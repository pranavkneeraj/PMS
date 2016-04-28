/**
 * Register controller
 * @namespace thinkster.authentication.controllers
 */
(function () {
  'use strict';

  angular
    .module('pms.accounts.controllers')
    .controller('AcademicDetailController', AcademicDetailController);

    AcademicDetailController.$inject = ['$location', '$scope', '$state', '$stateParams', 'UserService'];

  /**
   * @namespace
   */
    function AcademicDetailController($location, $scope, $state, $stateParams, UserService) {
        var vm = this;
        vm.alert_page = "static/templates/common/alert.html";
        vm.form_page = "static/templates/common/academic_detail_form.html";
        vm.studentAcademicDetail = {};
        if(!UserService.isLogin)
            vm.success_msg = "Your personal details are saved.";
        vm.error_msg = "";
        console.log("Inside academic controller", $stateParams);
        vm.add_academic_detail = function() {
            console.log(vm.studentAcademicDetail);
	    vm.studentAcademicDetail.student=$stateParams.student.id;
            UserService.academicDetailApi.save(vm.studentAcademicDetail).$promise.then(function (success) {
                console.log(success);
		vm.success_msg = "Your Academic details are saved.";
                //vm.studentAcademicDetail = {}
                //$state.go('pg_detail',{'academic_detail_id':success.student, no_of_sem:vm.studentAcademicDetail.current_pg_sem});
            }, function (error) {
                console.log(error);
                vm.error_msg = "Some problem in saving academic detail, Please try again later";
                //$state.go('pg_detail',{'academic_detail_id':4, no_of_sem:vm.studentAcademicDetail.current_pg_sem});
            });
            console.log(vm.studentAcademicDetail);
        };
    }
})();
