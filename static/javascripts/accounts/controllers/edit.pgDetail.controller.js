/**
 * Register controller
 * @namespace thinkster.authentication.controllers
 */
(function () {
  'use strict';

  angular
    .module('pms.accounts.controllers')
    .controller('EditPGDetailController', EditPGDetailController);

    EditPGDetailController.$inject = ['$location', '$scope', '$cookies', '$q', '$anchorScroll', 'UserService', 'pgSemDetail', 'academicDetail'];

  /**
   * @namespace
   */
    function EditPGDetailController($location, $scope, $cookies, $q, $anchorScroll, UserService, pgSemDetail, academicDetail) {
        console.log("inside pg detail edit");

        $location.hash('pgDetailForm');
        $anchorScroll();
        var vm = this;
        vm.isEditForm = true;
        vm.academic_detail_not_found = true;
        vm.academic_detail_not_found = false;
        var pgSemDetailBeforeModification = [];
        if(pgSemDetail && !pgSemDetail.$promise) {
            vm.pgSemDetail = pgSemDetail;
            vm.academic_detail_not_found = false;
        }
        else {
            if(pgSemDetail.$promise) {
                pgSemDetail.$promise.then(function (success) {
                    vm.pgSemDetail = success.pg_sem;
                    //pgSemDetailBeforeModification = vm.pgSemDetail;
                    vm.academic_detail_not_found = false;
                    console.log(success);
                    console.log(success.pg_sem);
                    if(success.pg_sem.length==0) {
                        vm.pg_detail_not_found = true;
                        vm.pgSemDetail = [{'academic':success.student, 'sem_number':null, 'marks':null, percentage:null, 'no_of_backlogs':null}];
                    }
                }, function(error) {
                    console.log(error);
                    if(error.status == 404) {
                        console.log(error)
                        vm.error_msg = "Your have to save academic details first";
                        // vm.pgSemDetail = [{'academic':null, 'sem_number':null, 'marks':null, percentage:null, 'no_of_backlogs':null}];
                    }
                    else
                        vm.error_msg = "Something goes wrong in loading your detail.";
                });
            }
        }
        //document.getElementById(hashId).focus();
        vm.edit = function() {
            vm.submitInProgress=true;
            if(vm.pg_detail_not_found) {
                data = vm.pgSemDetail[0];
                UserService.pgDetailApi.save(data).$promise.then(function (success) {
                    console.log(success);
                    vm.submitInProgress=false;
                    vm.success_msg = "Your PG Detail Updated Successfully";
                    vm.error_msg=null;
                }, function (error) {
                    console.log(error);
                    vm.submitInProgress=false;
                    vm.error_msg = "Unable to update your PG detail, please try again";
                });
            }
            else {
                var deferred = $q.defer();
                var promises = [];
                console.log("PGDeatailForm",PGDetail);
                for(var i=0;i<vm.pgSemDetail.length;i++) {
                    var data = {};
                    data['id']=vm.pgSemDetail[0].id;
                    data['marks'] = vm.pgSemDetail[i].marks;
                    data['percentage'] = vm.pgSemDetail.percentage;
                    data['no_of_backlogs'] = vm.pgSemDetail.no_of_backlogs;
                    promises.push(UserService.pgDetailApi.update({'id':data.id}, data));
                }
                console.log(promises);
                $q.all(promises).then(function (success) {
                    console.log(success);
                    vm.submitInProgress=false;
                    vm.success_msg = "Your PG Detail Updated Successfully";
                    deferred.resolve();
                }, function (error) {
                    console.log(error);
                    vm.submitInProgress=false;
                    vm.error_msg = "Unable to update your academic detail, please try again";
                    deferred.reject();
                });
                $location.hash('pgDetailForm');
                $anchorScroll();
            }
        };
    }
})();
