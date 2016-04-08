/**
 * Authentication
 * @namespac pms.authentication.services
 */
(function () {
    'use strict';

    angular
        .module('pms.layout.services')
        .factory('LayoutService', Layout);

    Layout.$inject = ['$http', '$resource'];

    /**
     * @namespace Authentication
     * @returns {Factory}
     */
    function Layout($http, $resource) {
        /**
         * @name Authentication
         * @desc The Factory to be returned
         */
        var NotificationApi = $resource('api/notification/:id/', {id: '@data.id'}, {
            'update': { method:'PATCH' }
        });
        var Layout = {
            NotificationApi:NotificationApi
        };

        return Layout;

    }
})();
