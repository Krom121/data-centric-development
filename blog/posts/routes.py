from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from blog import db
from blog.models import Post
from blog.posts.forms import PostForm

posts = Blueprint('posts', __name__)

"""

Below is the route for the user to able to create a post then be redireacted to the post 
page where all users can view each others posts.The user can also click on a link to
see the post detail.

Users can updated the posts that they have created, But only the ones they created
users can not updated anyother users post.A 403 error will be raised(forbidden response)

Users can also delete their own posts, current_user posts.

"""

@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('posts.post'))
    return render_template('create_post.html', title='Create Posts', form=form, legend='New Post')

"""

Below is the logic for the for the post route where 
all users can view each others post

"""

@posts.route("/post", methods=['POST', 'GET'])
@login_required
def post():

    posts = Post.query.all()
    return render_template('post.html', title='Posts', posts=posts)

"""

Below is the details of the full post post detail veiw

"""

@posts.route("/post/detail/<int:post_id>")
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post_detail.html', title=post.title, post=post)

"""

below is where the current user can update there post.

"""

@posts.route("/post/detail/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id = post_id))
    elif request.method == 'GET':    
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Posts', form=form, legend='Update Post')

"""

Below is the python logic for deleting a post by id.
Only the current user of that post can delete the post.

"""

@posts.route("/post/detail/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been Deleted!', 'danger')
    return redirect(url_for('posts.post'))