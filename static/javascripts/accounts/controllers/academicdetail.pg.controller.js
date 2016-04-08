/**
 * Register controller
 * @namespace thinkster.authentication.controllers
 */
(function () {
  'use strict';

  angular
    .module('pms.accounts.controllers')
    .controller('AcademicDetailPGController', AcademicDetailPGController);

    AcademicDetailPGController.$inject = ['$location', '$scope', '$stateParams', 'UserService'];

  /**
   * @namespace
   */
    function AcademicDetailPGController($location, $scope, $stateParams, UserService) {
        var vm = this;
        vm.submitInProgress = false;
        vm.pgSemDetail = [];
        vm.no_of_sem = parseInt($stateParams.no_of_sem);
        console.log("Inside pg controller", vm.no_of_sem);
        var add_sem_field = function () {
            for(var i=1; i<vm.no_of_sem;i++)
                vm.pgSemDetail[i-1] = {'academic':$stateParams.academic_detail_id, 'sem_number':null, 'marks':null, percentage:null, 'no_of_backlogs':null};
        };
        add_sem_field();
        vm.add_pg_detail = function() {
            vm.submitInProgress = false;
            console.log(vm.pgSemDetail, UserService);
            for(var i=0; i<vm.pgSemDetail.length; i++) {
                vm.pgSemDetail[i].sem_number = i+1;
                UserService.pgDetailApi.save(vm.pgSemDetail[i]).$promise.then(function (success) {
                    vm.success = true;
                    console.log(success);
                }, function (error) {
                    vm.error_msg = error.data;
                });
                console.log(vm.studentAcademicDetail);
            }
        };
    }
})();
