from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):           #Basis-Klasse für Custom Permissions
    """
    Custom permission to only allow owners of an object to edit it.
    Admins can also edit/delete any object.
    """
    
    def has_object_permission(self, request, view, obj):        #Wird für spezifische Objekte aufgerufen
        # Read permissions are allowed to any authenticated user
        if request.method in permissions.SAFE_METHODS:      # GET, HEAD, OPTIONS (nur Lesen)
            return True
        
        # Write permissions are only allowed to the owner or admin
        return obj.author == request.user or request.user.is_staff  #Nur der Autor oder Admin kann schreiben
    
    