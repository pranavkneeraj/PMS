from django.db import models
import uuid
from django.utils import timezone
class CreatedFlagModelMixin(models.Model):

    """
    Add a ```created_on``` field to the model. Set the value to datetime
    when the model is created.
    """
    created_on = models.DateTimeField(
        auto_now_add=True, editable=False, db_index=True
    )

    class Meta:
        abstract = True


class UpdatedFlagModelMixin(models.Model):

    """
    Add a ```updated_on``` field to the model. Set the value to datetime
    when the model is updated.
    """
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class DeletedFlagQuerySet(models.query.QuerySet):

    """Allows bulk deletion but with soft delete."""

    def delete(self):
        """set ```deleted_on``` field to current timestamp"""
        self.update(deleted_on=timezone.now())

    def restore(self):
        """set ```deleted_on``` field to ```None```"""
        self.update(deleted_on=None)


class DeletedManager(models.Manager):

    """
    Exclude objects that has ```deleted_on``` field set (by default).
    """

    def get_queryset(self, deleted_on__isnull=True):
        # pylint: disable = no-member
        """update all query set to filter in/out objects ```deleted_on``` """
        return DeletedFlagQuerySet(self.model, using=self._db).filter(
            deleted_on__isnull=deleted_on__isnull
        )

    def deleted(self):
        """get objects that have ```deleted_on``` value set"""
        return self.get_queryset(deleted_on__isnull=False)


class DeletedFlagModelMixin(models.Model):

    """
    Add a ```deleted_on``` field to the model. Set the value to datetime
    when the model is attempted to be deleted.
    """
    deleted_on = models.DateTimeField(
        blank=True, null=True, editable=False, db_index=True
    )
    objects = DeletedManager()

    def delete(self, *args, **kwargs):
        """
        update ```deleted_on``` field in the model to current timestamp
        """
        # pylint: disable=W0613
        self.deleted_on = timezone.now()
        self.save(update_fields=['deleted_on'])

    def restore(self):
        """
        update ```deleted_on``` field in the model to ```None```
        """
        self.deleted_on = None
        self.save(update_fields=['deleted_on'])

    def trash(self, *args, **kwargs):
        """
        permanently delete the model (not setting ```deleted_on``` flag)
        """
        super(DeletedFlagModelMixin, self).delete(*args, **kwargs)

    class Meta:
        abstract = True

    @property
    def is_deleted(self):
        """
        add a property ```is_deleted``` to the models which will have
        ```true``` or ```false``` depending on the value of ```deleted_on```
        """
        return bool(self.deleted_on)



class BaseModel(CreatedFlagModelMixin,
                UpdatedFlagModelMixin,
                DeletedFlagModelMixin,
                models.Model):

    """
    Base model from which other models will
    inherit.

    # Adds generic fields such as:
    - ```id``` which is a UUID field.
    - ```created_on```
    - ```updated_on```
    - ```deleted_on```
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    class Meta:
        abstract = True
