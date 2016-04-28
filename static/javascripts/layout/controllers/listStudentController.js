/**
 * IndexController
 * @namespace thinkster.layout.controllers
 */
(function () {
  'use strict';

  angular
    .module('pms.layout.controllers')
    .controller('studentListController', studentListController);
    studentListController.$inject = ['$scope', '$location', '$anchorScroll', '$uibModal', 'UserService'];

  /**
   * @namespace IndexController
   */
    function studentListController($scope, $location, $anchorScroll, $uibModal, UserService) {
        var vm = this;
        vm.students = [];
        $scope.currentPage = 1;
        vm.itemsPerPage = 10;
        vm.maxSize = 5;
        vm.sort_by = '-address';
        console.log("dsaas",UserService);
        UserService.api.query().$promise.then(
            function (success) {
                vm.students = success;
                vm.filteredStudents = success;
                vm.totalItems = success.length;
                console.log("dasdsadasdsadsad",success.length);
                $anchorScroll('content-area');
                //console.log(angular.element(document).find('#bottom'))
            }, function (error) {
                console.log("error",error);
            }
        );
        vm.filterStudent = function() {
            vm.filteredStudents=[];
            for(var i=0;i<vm.students.length;i++) {
                var match = true;
                for(var j=0;j<vm.selectedStudent.length;j++) {
                    if(vm.students[i].first_name.indexOf(vm.selectedStudent[j])<0){
                        match = false;
                        break;
                    }
                }
                if(match)
                    vm.filteredStudents.push(vm.students[i]);
            }
            if(i==0)
                vm.filteredStudents=vm.students
        };

        vm.editPersonalDetail = function (selectedStudent) {
            vm.selectedStudent = selectedStudent;
            console.log("student", selectedStudent)
            var modalInstance = $uibModal.open({
                templateUrl:'static/templates/authentication/edit_personal_detail_modal.html',
                windowClass: '',
                size: 'bg',
                controller:'EditPersonalDetailByAdminController',
                controllerAs:'vm',
                scope:'',
                resolve: {
                    'student':function() {
                        return vm.selectedStudent;
                    }
                }
            });
            modalInstance.result.then(function (success) {
                console.log("asdadasd");
            });
        };
        vm.editAcademicDetail = function (selectedStudent) {

            vm.selectedStudent = selectedStudent;
            console.log("student", selectedStudent)
            var modalInstance = $uibModal.open({
                templateUrl:'static/templates/authentication/edit_academic_detail_modal.html',
                windowClass: '',
                size: 'bg',
                controller:'EditAcademicDetailByAdminController',
                controllerAs:'vm',
                scope:'',
                resolve: {
                    'academic_detail_id':function() {
                        return vm.selectedStudent.id;
                    }
                }
            });
            modalInstance.result.then(function (success) {
                console.log("asdadasd");
            });
        };
        vm.editPGDetail = function (selectedStudent) {
            vm.selectedStudent = selectedStudent;
            console.log("student", selectedStudent);
            var modalInstance = $uibModal.open({
                templateUrl:'static/templates/authentication/edit_pg_detail_modal.html',
                windowClass: '',
                size: 'bg',
                controller:'EditPGDetailByAdminController',
                controllerAs:'vm',
                scope:'',
                resolve: {
                    academicDetail: function(){
                        return null;
                    },
                    pgSemDetail:function(UserService){
                        return UserService.academicDetailApi.get({'id':vm.selectedStudent.id, 'include_pg_sem':'t'});
                    }
                }

            });
            modalInstance.result.then(function (success) {
                console.log("asdadasd");
            });
        };


        vm.update = function () {
        };
        vm.remove = function (selectedStudent) {
            var modalInstance = $uibModal.open({
                animation: $scope.animationsEnabled,
                templateUrl: 'static/templates/common/modal_alert.html ',
                controller:'alertModalController',
                controllerAs:'vm',
                resolve:{
                    msg:function(){
                        return "Do you want delete this student?";
                    }
                }
            });

            modalInstance.result.then(function(success){
                UserService.api.remove({'id':selectedStudent.id}).$promise.then(
                    function (success) {
                        console.log("deleted");
                        console.log(angular.element(document).find('#'+selectedStudent.id))
                        angular.element(document).find('#'+selectedStudent.id).remove();
                    }, function (error) {
                        console.log("error",error)
                    }
                );
            });
        };
    };

})();
