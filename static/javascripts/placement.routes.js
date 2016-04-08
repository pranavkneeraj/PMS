(function () {
    'use strict';

    angular
        .module('placement.routes')
        .config(config);

    config.$inject = ['$urlRouterProvider', '$stateProvider'];
    /**
     * @name config
     * @desc Define valid application routes
   */
    function config($urlRouterProvider, $stateProvider) {

        $stateProvider
            .state('home', {
                url: '/',
                templateUrl: '/static/templates/pages/default.html'
            })
            .state('register_not_jica', {
                url: '/register',
                controller: 'RegisterController',
                controllerAs: 'vm',
                resolve: {
                    student: function(){
                        return null;
                    }
                },
                templateUrl: '/static/templates/authentication/register.html'
            })
            .state('academic_detail', {
                url: 'register/academic_detail',
                templateUrl: '/static/templates/authentication/add_academic_detail.html',
                controller:'AcademicDetailController',
                controllerAs:'vm',
                params :{
                    student:null
                }
            })
            .state('pg_detail', {
                url: 'register/academic_detail/pg_detail',
                templateUrl: '/static/templates/accounts/pg_detail.html ',
                controller:'AcademicDetailPGController',
                controllerAs:'vm',
                params :{
                    academic_detail_id:null,
                    no_of_sem: null
                }
            })
            .state('edit_personal_detail', {
                url: '/edit/personal_detail',
                controller: 'EditPersonalDetailController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/authentication/register.html'
            })
            .state('edit_academic_detail', {
                url: 'edit/academic_detail',
                templateUrl: '/static/templates/authentication/add_academic_detail.html',
                controller:'EditAcademicDetailController',
                controllerAs:'vm',
                params :{
                    student:null
                },
                resolve: {
                    academic_detail: function(){
                        return null;
                    }
                }
            })
            .state('edit_pg_detail', {
                url: 'edit/academic_detail/pg_detail',
                templateUrl: '/static/templates/accounts/pg_detail.html ',
                controller:'EditPGDetailController',
                controllerAs:'vm',
                resolve: {
                    academicDetail: function(){
                        return null;
                    },
                    pgSemDetail:function(UserService){
                        return UserService.academicDetailApi.get({'id':UserService.user.id, 'include_pg_sem':'t'});
                    }
                }
            })
            .state('register', {
                url: '/register/{code:[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}}',
                templateUrl: '/static/templates/authentication/register.html',
                controller: 'RegisterController',
                controllerAs: 'vm',
                resolve: {
                    student: function(UserService, $location){
                        var code = $location.path().split('/')[2];
                        return UserService.codeApi.get({'code':code, 'include_user':'t'});
                    }
                }
            })
            .state('login', {
                url: 'login',
                controller: 'LoginController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/authentication/login.html'
            })
            .state('add_students_manual', {
                url: '/add_students/manual',
                controller: 'studentController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/pages/add_student.html'
            })
            .state('add_students_from_excel_file', {
                url: '/add_students/excel',
                templateUrl: '/static/templates/pages/add_student_from_excel.html',
                controller: 'addStudentByExcelController',
                controllerAs: 'vm',
            })
            .state('list_students', {
                url: '/list_student',
                controller: 'studentListController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/pages/student_list.html'
            });

        // $routeProvider.when('/', {
        //     controller: '',
        //     controllerAs: 'vm',
        // templateUrl: '/static/templates/pages/default.html'
        // }).when('/register/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', {

        // },

        // ).when('/register', {

        // }).when('/login', {
        //       }).when('/add_student', {
        //     controller: 'studentController',
        //     controllerAs: 'vm',
        //     templateUrl: '/static/templates/pages/add_student.html'
        // }).when('/list_student', {

        // });

  }
})();
