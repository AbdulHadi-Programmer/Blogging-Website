# Deadline 31 March 2025 12 am :

## Today is 29 March (4 pm)
- The Project name is Personal Blogging Website :
1. Basic User System
  - User login, logout, signup (by using django builtin authentication)
  - Admin Dashboard (Django Admin)

2. Blog Post Management
  - Create, Edit, Delete and Update blog posts 
  - Store posts in the database (SQlite for now )
  - Publish / Unpublish feature

3. Categories and Tag 
  - Categorize posts
  - Add tags for filtering 

4. SEO-Friendly URLs
  - Slug Based URLs (`/blog/how-to-start-django/` instead of `/blog/1/`)

5. Basic Comment System 
  - Allow users (or just yourself) to comment on posts

### Project Structure :
1. Models :

1. **Blog Post Model (Main Content Storage)**
`Done`

2. **Views (Essential Views)** 
- HomePage View -- List All Blog Post
- Blog Detail View -- Show a complete Blog Post
- Create a blog view -- Simple form to add new posts (only for admin)

3. **URLs (Minimal)**
- `'/'` HomePage (List of Posts)
- `'/blog/<slug>/'` Blog Post detail
- `'/blog/new/'`  Create new post - but only display or visit when a user is admin 

4. **Templates (Using Templates and Bootstrap)**
- **home.html** -> Show All Posts 
- **blog_detail.html** -> Show Full Post with Complete Detail (content)
- **new_post.html** -> Single form for adding new posts 



Field	          |  Purpose
category	      |  Allows filtering by category in views and templates.
is_published    |	Lets you write drafts without making them visible.
cover_image	    | If you want to show a thumbnail image for the blog post.
Category model	Helps organize your posts cleanly.