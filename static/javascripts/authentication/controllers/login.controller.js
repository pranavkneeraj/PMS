/**
* LoginController
* @namespace pms.authentication.controllers
*/
(function () {
  'use static';

  angular
    .module('pms.authentication.controllers')
    .controller('LoginController', LoginController);  

  LoginController.$inject = ['$location', '$scope', '$cookies', 'Authentication', 'UserService'];

  /**
  * @namespace LoginController
  */
  function LoginController($location, $scope, $cookies, Authentication, UserService) {
    var vm = this;
    vm.login = login;
    /**
    * @name login
    * @desc Log the user in
    * @memberOf pms.authentication.controllers.LoginController
    */
    function login() {
      console.log("inside login")
      Authentication.login(vm.email, vm.password).then(function(success){
        UserService.isLogin = true;
        delete success.data['password']
        UserService.user  = success.data;
        $cookies.putObject('user', UserService.user)
        $scope.isLogin = UserService.isLogin;
        console.log(UserService, $scope)
        $location.path("/")
      }, function(error){
        UserService.isLogin = false;
        UserService.user  = null;
      });
    }
  }
})();
