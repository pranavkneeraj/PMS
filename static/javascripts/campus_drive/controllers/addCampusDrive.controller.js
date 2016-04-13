/**
 * IndexController
 * @namespace thinkster.layout.controllers
 */
(function () {
  'use strict';

  angular
        .module('pms.campusdrive.controllers')
        .controller('addCampusDriveController', addCampusDriveController);
    addCampusDriveController.$inject = ['$scope','$uibModal', '$anchorScroll', 'UserService'];

  /**
   * @namespace IndexController
   */

    function addCampusDriveController($scope, $uibModal, $anchorScroll, UserService) {
        var vm = this;
        vm.alert_page = "static/templates/common/alert.html ";
        vm.form_page = "static/templates/common/campus_drive_form.html";
        vm.campusDrive = {};
        $scope.specialCriteriaFlag = {
            option:true
        };
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
        vm.yes = true;
        vm.no = false;

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
        vm.add_campus_drive = function() {
            //vm.submitInProgress = true;
            console.log(vm.campusDrive);
            if($scope.specialCriteriaFlag.option=='yes')
                add_and_save_special_criteria();
            else
                vm.have_special_criteria = false;
            UserService.campusDriveApi.save(vm.campusDrive).$promise.then(function(success) {
                vm.success_msg = "Campus drive added successfully";
                console.log(success);
                vm.campusDrive = success;
                vm.submitInProgress = false;
                $anchorScroll('content-area');
            }, function(error) {
                vm.error_msg = "Campus drive not created, please try again";
                console.log(error)
                vm.submitInProgress = false;
                $anchorScroll('content-area');
            });
        };

        vm.add_special_criteria = function() {
            var modalInstance = null;
            console.log("Inside special");
            vm.submitInProgress = true;
            var data = vm.specialCriteria;
            data['campus_drive'] = vm.campusDrive.id;
            data['criteria_for'] = vm.criteria_for.selectedOption.name;
            UserService.specialCriteriaApi.save(data).$promise.then(function(success) {
                vm.success_msg = "special Criteria is  added successfully";
                console.log(success)
                vm.submitInProgress = false;
                $anchorScroll('content-area');
            }, function(error) {
                vm.error_msg = "Special criteria not added, please try again";
                console.log(error)
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
            });
            if(modalInstance){
                modalInstance.result(function(success){
                    console.log("success",success)
                },function(error){
                    console.log("error",error)
                });
            }
        };

        function add_and_save_special_criteria() {
            vm.form_page = "static/templates/common/special_criteria_form.html";
            vm.criteria_for = {
                availableOptions: [
                    {value: 'ssc', name: 'SSC'},
                    {value: 'hsc', name: 'HSC'},
                    {value: 'ug', name: 'UG'},
                    {value: 'pg', name: 'PG'},
                    {value: 'other', name: 'Other'},

                ],
                selectedOption: {value: 'ssc', name: 'SSC'} //This sets the default value of the select in the ui

            };
        }

        };
    })();
