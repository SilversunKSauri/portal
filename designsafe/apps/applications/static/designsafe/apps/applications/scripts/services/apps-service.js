(function(window, angular, $, _) {  "use strict";  angular.module('ApplicationsApp').factory('Apps', ['$http', '$q', 'djangoUrl', function($http, $q, djangoUrl) {    var service = {};    var default_list_opts = {      publicOnly: false    };    service.list = function(query) {      return $http({        url: djangoUrl.reverse('designsafe_applications:call_api', ['meta']),        method: 'GET',        params: {'q': query}      });    };    service.get = function(app_id) {      return $http({        url: djangoUrl.reverse('designsafe_applications:call_api', ['apps']),        method: 'GET',        params: {'appId': app_id}      });    };    service.getPermissions = function(app_id) {      return $http({        url: djangoUrl.reverse('designsafe_applications:call_api', ['apps']),        method: 'GET',        params: {'appId': app_id, 'pems': true}      });    };    service.getMeta = function(app_id) {      return $http({        url: djangoUrl.reverse('designsafe_applications:call_api', ['meta']),        method: 'GET',        params: {q:{'name': 'ds_app','value.id': app_id}}      });    };    service.createApp = function(body) {      return $http({        url: djangoUrl.reverse('designsafe_applications:call_api', ['apps']),        method: 'POST',        data: body      });    };    service.createMeta = function(body) {      return $http({        url: djangoUrl.reverse('designsafe_applications:call_api', ['meta']),        method: 'POST',        data: body      });    };    service.updateMeta = function(body, uuid) {      return $http({        url: djangoUrl.reverse('designsafe_applications:call_api', ['meta']),        method: 'POST',        data: body,        params: {'uuid': uuid},      });    };    service.updateMetaPermissions = function(permission, uuid) {      console.log('permission');      console.log(permission);      console.log('uuid');      console.log(uuid);      return $http({        url: djangoUrl.reverse('designsafe_applications:call_api', ['meta']),        method: 'POST',        data: permission,        params: {'uuid': uuid, 'username': permission.username, 'pems': true}      })    };    service.manageApp = function(appId, body){      return $http({        url: djangoUrl.reverse('designsafe_applications:call_api', ['apps']),        method: 'POST',        data: body,        params: {'appId': appId}      });    }    service.deleteApp = function(app_id){      return $http({        url: djangoUrl.reverse('designsafe_applications:call_api', ['apps']),        method: 'DELETE',        params: {'appId': app_id},      });    }    service.deleteMeta = function(uuid){      return $http({        url: djangoUrl.reverse('designsafe_applications:call_api', ['meta']),        method: 'DELETE',        params: {'uuid': uuid},      });    };    service.getSystems = function(system_id, isPublic, type){      return $http({        url: djangoUrl.reverse('designsafe_applications:call_api', ['systems']),        method: 'GET',        params: {'system_id': system_id, 'type': type}      });    };     service.getFile = function(system_id, path){      return $http({        url: djangoUrl.reverse('designsafe_applications:call_api', ['files']),        method: 'GET',        params: {'system_id': system_id, 'path': path}      });    };    return service;  }]);})(window, angular, jQuery, _);