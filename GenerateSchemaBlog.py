import streamlit as st
import json

st.title("Educational Blog JSON-LD Schema Generator")

# --- Blog Details ---
st.header("Blog Details")
headline = st.text_input("Blog Headline", "Master Excel Formulas for Business Analytics")
description = st.text_area("Blog Description", "Learn the top Excel formulas every marketer and data analyst should know.")
author_name = st.text_input("Author Name", "Siddharth")
author_url = st.text_input("Author URL", "https://www.yourdomain.com/about")
publisher_name = st.text_input("Publisher Name", "Siddharth Computer Institute")
publisher_logo = st.text_input("Publisher Logo URL", "https://www.yourdomain.com/images/logo.png")
blog_url = st.text_input("Blog URL", "https://www.yourdomain.com/blog/excel-formulas")
date_published = st.date_input("Date Published")
date_modified = st.date_input("Date Modified")
keywords = st.text_input("Keywords (comma separated)", "Excel Training, Business Analytics, Education, Marketing Skills")
article_section = st.text_input("Article Section", "Education")

# --- Images ---
st.header("Blog Images")
images = []
num_images = st.number_input("Number of Images", min_value=0, max_value=5, value=2)
for i in range(num_images):
    st.subheader(f"Image {i+1}")
    img_url = st.text_input(f"Image URL {i+1}", "")
    img_caption = st.text_input(f"Image Caption {i+1}", "")
    if img_url:
        images.append({"@type": "ImageObject", "url": img_url, "caption": img_caption})

# --- Video ---
st.header("Blog Video (optional)")
video_name = st.text_input("Video Name", "")
video_desc = st.text_area("Video Description", "")
video_thumbnail = st.text_input("Video Thumbnail URL", "")
video_content = st.text_input("Video Content URL", "")
video_embed = st.text_input("Video Embed URL", "")
video_duration = st.text_input("Video Duration (ISO 8601, e.g., PT5M30S)", "")

video = {}
if video_name and video_content:
    video = {
        "@type": "VideoObject",
        "name": video_name,
        "description": video_desc,
        "thumbnailUrl": video_thumbnail,
        "uploadDate": str(date_published),
        "contentUrl": video_content,
        "embedUrl": video_embed,
        "duration": video_duration
    }

# --- Courses ---
st.header("Related Courses")
courses = []
num_courses = st.number_input("Number of Courses", min_value=0, max_value=5, value=2)
for i in range(num_courses):
    st.subheader(f"Course {i+1}")
    course_name = st.text_input(f"Course Name {i+1}", "")
    course_desc = st.text_area(f"Course Description {i+1}", "")
    course_url = st.text_input(f"Course URL {i+1}", "")
    if course_name and course_url:
        courses.append({
            "@type": "Course",
            "name": course_name,
            "description": course_desc,
            "provider": {
                "@type": "Organization",
                "name": publisher_name,
                "sameAs": blog_url
            },
            "url": course_url
        })

# --- Related Links ---
st.header("Related Links (Internal/External)")
related_links = []
num_links = st.number_input("Number of Related Links", min_value=0, max_value=5, value=2)
for i in range(num_links):
    link_name = st.text_input(f"Link Name {i+1}", "")
    link_url = st.text_input(f"Link URL {i+1}", "")
    if link_name and link_url:
        related_links.append({"@type": "WebPage", "name": link_name, "url": link_url})

# --- Generate JSON-LD ---
if st.button("Generate JSON-LD Schema"):
    schema = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": headline,
        "description": description,
        "author": {
            "@type": "Person",
            "name": author_name,
            "url": author_url
        },
        "publisher": {
            "@type": "Organization",
            "name": publisher_name,
            "logo": {
                "@type": "ImageObject",
                "url": publisher_logo
            }
        },
        "datePublished": str(date_published),
        "dateModified": str(date_modified),
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": blog_url
        },
        "articleSection": article_section,
        "keywords": [k.strip() for k in keywords.split(",")],
    }

    if images:
        schema["image"] = images
    if video:
        schema["video"] = video
    if courses:
        schema["mentions"] = courses
    if related_links:
        schema["relatedLink"] = [link["url"] for link in related_links]  # Google accepts relatedLink as list of URLs

    st.subheader("Generated JSON-LD Schema")
    st.code(json.dumps(schema, indent=2), language="json")
