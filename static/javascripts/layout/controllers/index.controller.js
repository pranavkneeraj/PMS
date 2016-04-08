/**
 * IndexController
 * @namespace thinkster.layout.controllers
 */
(function () {
    'use strict';

    angular
        .module('pms.layout.controllers')
        .controller('IndexController', IndexController)
        .controller('NotificationController', NotificationController);

    IndexController.$inject = ['$scope', '$location', '$cookies', 'UserService', 'Authentication'];

    NotificationController.$inject = ['$scope', '$location', '$cookies', 'LayoutService'];

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
                $location.path('/');
            }
        };
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

})();
