/**
 * IndexController
 * @namespace thinkster.layout.controllers
 */
(function () {
  'use strict';

  angular
    .module('pms.layout.controllers')
    .controller('addStudentByExcelController', addStudentByExcelController);
    addStudentByExcelController.$inject = ['$scope', 'Upload', '$location', '$anchorScroll'];

  /**
   * @namespace IndexController
   */

    function addStudentByExcelController($scope, Upload, $location, $anchorScroll) {
        var vm = this;
        vm.data= "sdad";

        vm.submitInProgress = false;
        vm.uploadExcelFile = function(file) {
            file.upload = Upload.upload({
                url: 'api/user/add_users/',
                data: {file: file}
            });
            file.upload.then(function(success) {
                vm.success_msg = success.data;
                console.log(success.data);
             }, function(error) {
                 console.log(error)
             });
            // console.log(vm.excelFile.type);
            // console.log("sadasd");
            // var fdata = new FormData();
            // fdata.append("file", vm.excelFile);
            // UserService.addStudentList.postWithFile({'file':fdata}).$promise.then(function(success) {
            //     console.log(success);
            // }, function(error) {
            //     console.log(error)
            // });
        };
  }
})();
