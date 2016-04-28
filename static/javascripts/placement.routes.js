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
                url: '/register/academic_detail',
                templateUrl: '/static/templates/authentication/add_academic_detail.html',
                controller:'AcademicDetailController',
                controllerAs:'vm',
                params :{
                    student: function (UserService) { return UserService.user }
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
                controller: 'EditPersonalDetailByUserController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/authentication/register.html'
            })
            .state('edit_academic_detail', {
                url: 'edit/academic_detail',
                templateUrl: '/static/templates/authentication/add_academic_detail.html',
                controller:'EditAcademicDetailByUserController',
                controllerAs:'vm',
                params :{
                    student:null
                }
            })
            .state('edit_pg_detail', {
                url: 'edit/academic_detail/pg_detail',
                templateUrl: '/static/templates/accounts/pg_detail.html ',
                controller:'EditPGDetailByUserController',
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
                        var student_id = $location.path().split('/')[2];
                        return UserService.api.get({'id':student_id});
                    }
                }
            })
            .state('login', {
                url: '/login',
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
            .state('add_campus_drive', {
                url: '/add_campus_drive',
                templateUrl: '/static/templates/pages/add_campus_drive.html',
                controller: 'addCampusDriveController',
                controllerAs: 'vm'
            })
            .state('list_campus_drive', {
                url: '/list_campus_drive',
                templateUrl: '/static/templates/pages/list_campus_drive.html',
                controller: 'campusDriveListController',
                controllerAs: 'vm'
            })

            .state('list_students', {
                url: '/list_student',
                controller: 'studentListController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/pages/student_list.html'
            })
	    .state('list_students_by_campus_drive', {
                url: '/campus_drive/list_student',
                controller: 'studentListByCampusDriveController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/pages/list_student_by_campus_drive.html'
            })
	    .state('show_interest', {
                url: '/student/placement/campusdrive_interest',
                templateUrl: '/static/templates/pages/campus_drive_interest.html'
            })
	    

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
