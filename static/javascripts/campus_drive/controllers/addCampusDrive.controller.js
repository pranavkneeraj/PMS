/**
 * IndexController
 * @namespace thinkster.layout.controllers
 */
(function () {
  'use strict';

  angular
        .module('pms.campusdrive.controllers')
        .controller('addCampusDriveController', addCampusDriveController);
    addCampusDriveController.$inject = ['$scope','$uibModal', '$location', '$anchorScroll', 'UserService'];

  /**
   * @namespace IndexController
   */

    function addCampusDriveController($scope, $uibModal, $location, $anchorScroll, UserService) {
        var vm = this;
        vm.alert_page = "static/templates/common/alert.html ";
        vm.form_page = "static/templates/common/campus_drive_form.html";
        vm.form_title = "Add Campus Drive";
        vm.campusDrive = {};
        $anchorScroll('content-area');
        $scope.datePicker = {
            opened:false
        };
        $scope.dt = new Date()
        $scope.inlineOptions = {
            minDate: new Date(),
            showWeeks: true
        };
        $scope.minDate = $scope.dt;
        $scope.showWeeks = false;
        $scope.open = function($event) {
            //$event.preventDefault();
            //$event.stopPropagation();
            $scope.datePicker.opened = true;
        };
        var get_batch_year_list = function() {
            var date = new Date();
            var year = date.getFullYear();
            var year_list = [];
            for(var i=0; i<10;i++) {
                year_list[i] = year--;
            }
            return year_list;
        };

        vm.batch_year_availableOptions= get_batch_year_list();
        vm.course_list_availableOptions = ['MCA', 'MSc(Computer Science)', 'BE/B.Tech','UG', 'UG Except BE/B.Tech'];
        vm.add_campus_drive = function() {
            vm.submitInProgress = true;
            // console.log(vm.campusDrive);
            // if($scope.specialCriteriaFlag.option=='yes')
            //     add_and_save_special_criteria();
            // else
            //vm.have_special_criteria = false;
            UserService.campusDriveApi.save(vm.campusDrive).$promise.then(function(success) {
                vm.success_msg = "Campus drive added successfully";
                vm.error_msg = null;
                console.log(success);
                vm.submitInProgress = false;
                $anchorScroll('content-area');
                if(vm.campusDrive.criteria_type == 'general' || vm.campusDrive.criteria_type=='both'){
                    vm.add_criteria();
                }
                if(vm.campusDrive.criteria_type == 'special'){
                    add_and_save_special_criteria();
                }
                vm.campusDrive = success;

            }, function(error) {
                vm.success_msg = null;
                vm.error_msg = "Campus drive not created, please try again";
                console.log(error);
                vm.submitInProgress = false;
                $anchorScroll('content-area');
            });
        };
        vm.add_criteria = function () {
            vm.form_page = "static/templates/common/criteria_form.html";
            vm.form_title = "Enter General Criteria for Campus Drive";
        };
        vm.save_criteria = function() {
            vm.criteria.campus_drive =  vm.campusDrive.id;
            UserService.criteriaApi.save(vm.criteria).$promise.then(function (success) {
                console.log(success);
                vm.submitInProgress = true;
                console.log(vm.campusDrive);
                if(vm.campusDrive.criteria_type=='both')
                    add_and_save_special_criteria();
                vm.error_msg=null;
                vm.success_msg = "Criteria added for campus drive";
            }, function(error) {
                console.log(error);
            });
        };
        vm.add_special_criteria = function() {
            var modalInstance = null;
            console.log("Inside special");
            vm.submitInProgress = true;
            var data = vm.specialCriteria;
            data['campus_drive'] = vm.campusDrive.id;
            data['criteria_for'] = vm.specialCriteria.criteria_for.value;
            UserService.specialCriteriaApi.save(data).$promise.then(function(success) {
                vm.success_msg = "special Criteria is  added successfully";
                console.log(success)
                vm.submitInProgress = false;
                $anchorScroll('content-area');
                modalInstance = $uibModal.open({
                    animation: $scope.animationsEnabled,
                    templateUrl: 'static/templates/common/modal_alert.html ',
                    controller:'alertModalController',
                    controllerAs:'vm',
                    resolve:{
                        msg:function(){
                            return "Do you want to add more special criteria for same campus drive?"
                        }
                    }
                });
                modalInstance.result.then(function(success){
                    vm.success_msg= "Add Next Special Criteria";
                    add_and_save_special_criteria();
                },function(error){
                    $location.path("/");
                });
            }, function(error) {
                vm.error_msg = "Special criteria not added, please try again";
                console.log(error)
                vm.submitInProgress = false;
                $anchorScroll('content-area');
            });

        };

        function add_and_save_special_criteria() {
            vm.form_page = "static/templates/common/special_criteria_form.html";
            vm.form_title = "Add special criteria For campus Drive";
            vm.specialCriteria = {criteria_for:{value: 'ssc', name: 'SSC'}};
            vm.criteria_for = {
                availableOptions: [
                    {value: 'ssc', name: 'SSC'},
                    {value: 'hsc', name: 'HSC'},
                    {value: 'ug', name: 'UG'},
                    {value: 'pg', name: 'PG'},
                    {value: 'other', name: 'Other'},

                ]
            };

        }

    };
})();
