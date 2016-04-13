/**
 * IndexController
 * @namespace thinkster.layout.controllers
 */
(function () {
    'use strict';

    angular
        .module('pms.layout.controllers')
        .controller('IndexController', IndexController)
        .controller('NotificationController', NotificationController)
        .controller('alertModalController', alertModalController);
    IndexController.$inject = ['$scope', '$location', '$cookies', 'UserService', 'Authentication'];

    NotificationController.$inject = ['$scope', '$location', '$cookies', 'LayoutService'];

    alertModalController.$inject = ['$uibModalInstance', 'msg'];

    /**
     * @namespace IndexController
     */
    function IndexController($scope, $location, $cookies, UserService, Authentication) {

        var vm = this;
        var user = $cookies.getObject('user');
        var activate = function () {
            if (user) {
                UserService.user = user ;
                UserService.isLogin = true;
//                $location.path('/');
            }
        };
        $scope.myInterval = 3000;

        $scope.noWrapSlides = false;

        $scope.active = 0;

        var slides = $scope.slides = [];

        var currIndex = 0;
        slides.push({

            image: 'static/images/j.jpg',

            text: ['Nice image','Awesome photograph','That is so cool','I love that'][slides.length % 4],

            id: currIndex++

        });
        slides.push({

            image: 'static/images/JICA-2.jpg',

            text: ['Nice image','Awesome photograph','That is so cool','I love that'][slides.length % 4],

            id: currIndex++

        });
        activate();
        vm.UserService = UserService;
        $scope.isLogin = UserService.isLogin;
        $scope.user = UserService.user;
        vm.logout = function () {
            Authentication.logout().then(function() {
                $cookies.remove('user');
                UserService.user='';
                UserService.isLogin=false;
            });;
        };
    }
    function NotificationController($scope, $location, $cookies, LayoutService) {
        var vm = this;
        $scope.currentPage = 1;
        vm.itemsPerPage = 5;
        vm.maxSize = 5;
        console.log("inside Notification", LayoutService, (($scope.currentPage-1)*vm.itemsPerPage), (($scope.currentPage)*vm.itemsPerPage));
        LayoutService.NotificationApi.query().$promise.then(function(success) {
            vm.notifications = success;
            $scope.totalItems=success.length;
            console.log(success);;
        });
        vm.pageChanged = function(){
            console.log("asds");
        };
    }

    function alertModalController($uibModalInstance, msg) {
        console.log("alert")
        var vm = this;
        vm.msg = msg;
        vm.close = function(){
            console.log("close")
            $uibModalInstance.close();
        };
        vm.dismiss = function(){
            console.log("close")

            $uibModalInstance.dismiss();
        };
    }

})();
