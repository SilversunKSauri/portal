/**
 * This service is currently a stub service static data. We don't need dynamic system
 * lookup right now, but it will be nicer to go ahead and code against this service
 * rather than having stubs all over the place.
 */
(function(window, angular, $, _) {
  'use strict';
  angular.module('designsafe').factory('Systems', ['$q', '$http', 'djangoUrl', function($q, $http, djangoUrl) {
    var service = {};

    var systemsList = [
        {
          id: 'designsafe.storage.default',
          name: 'My Data',
          storage: {
              homeDir: '/',
              rootDir: '/corral-repl/tacc/NHERI/shared'
          },
          type: 'STORAGE',
          uuid: '5072762172135903717-242ac114-0001-006',
          fileMgr: 'agave',
          baseUrl: '/api/agave/files'
        },
        {
          id: 'designsafe.storage.projects',
          name: 'My Projects',
          storage: {
            homeDir: '/',
            rootDir: '/corral-repl/tacc/NHERI/projects'
          },
          type: 'STORAGE',
          uuid: '5762770863681049062-242ac117-0001-006', // UUID seems to be unused
          fileMgr: 'projects',
          baseUrl: '/api/projects/files'
        },
        {
          id: 'nees.public',
          name: 'Published',
          storage: {
            homeDir: '/',
            rootDir: '/corral-repl/tacc/NHERI/public/projects'
          },
          type: 'STORAGE',
          uuid: '8688297665752666597-242ac119-0001-006',
          fileMgr: 'public',
          baseUrl: '/api/public/files'
        },
    ];

    service.getMonitor = function(system_id) {
      return $http({
        url: djangoUrl.reverse('designsafe_workspace:call_api', ['monitors']),
        method: 'GET',
        params: {'target': system_id},
        cache: false
      });
    };

    service.list = function() {
      return $q(function(resolve, reject) {
        resolve(systemsList);
      });
    };

    service.get = function(systemId) {
      return $q(function(resolve, reject) {
        var system;
        for (var s in systemsList) {
          if (s.id === systemId) {
            system = s;
            break;
          }
        }
        if (system) {
          resolve(system);
        } else {
          reject(system);
        }
      });
    };

    return service;
  }]);
})(window, angular, jQuery, _);
