var Campground = require("../models/campground");
var Comment = require("../models/comment");
//all middleware
var middlewareObj ={};

middlewareObj.checkCampgroundOwnership = function (req, res, next){
        if(req.isAuthenticated()){
          Campground.findById(req.params.id, function(err, foundCampground){
               if(err){
                   req.flash("error", "It is not found");
                   res.redirect("back");
               } else {
                   if(foundCampground.author.id.equals(req.user._id) || req.user.isAdmin){
                       next();
                   } else {
                       req.flash("error", "You don't have permission");
                       res.redirect("back");
                   }
               }
            });
    } else {
        req.flash("error", "You need to be logged in to do that!");
        res.redirect("back");
    }
}

middlewareObj.checkCommentOwnership = function (req, res, next){
        if(req.isAuthenticated()){
          Comment.findById(req.params.comment_id, function(err, foundComment){
               if(err){
                   res.redirect("back");
               } else {
                   if(foundComment.author.id.equals(req.user._id) || req.user.isAdmin){
                       next();
                   } else {
                       req.flash("error", "You don't have permission!");
                       res.redirect("back");
                   }
               }
            });
    } else {
        req.flash("error", "You need to log in first!");
        res.redirect("back");
    }
}

middlewareObj.isLoggedIn = function (req, res, next){
    if(req.isAuthenticated()){
        return next();
    }
    req.flash("error", "Come on! You need to login first!");
    res.redirect("/login");
}

module.exports = middlewareObj