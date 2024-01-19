function liked(id){
    var element = document.getElementById("like_"+id);
    element.classList.toggle("liked");
    var like = document.getElementById("dislike_"+id);
    like.classList.remove("liked");
}

function disliked(id){
    var dislike = document.getElementById("dislike_"+id);
    dislike.classList.toggle("liked");
    var like = document.getElementById("like_"+id);
    like.classList.remove("liked");
}