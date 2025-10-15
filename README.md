# GenerateSchema
Generate JSON-LD Schema -  the app builds the entire schema dynamically

Educational Blog JSON-LD Schema Generator

A Streamlit-based app that generates JSON-LD structured data for educational blogs. This app allows content creators and educators to enhance SEO, link related courses, include videos and images, and add related links in their blog posts.

🔹 Table of Contents

Overview

Features

Installation

Usage

Example Schema Output

Contributing

License

🔹 Overview

Structured data (JSON-LD) helps search engines understand your content better and can improve visibility with rich search results. This app is specifically designed for educational blogs covering topics like marketing, Excel, Power BI, and other technical subjects.

The app allows you to create a JSON-LD schema that includes:

Blog details (title, description, author, publisher)

Multiple images with captions

Video content with thumbnails and duration

Related courses with URLs and descriptions

Internal or external related links

🔹 Features

✅ Blog Details Input – Headline, description, author, publisher, dates, keywords, and article section.
✅ Images – Add multiple images with captions using ImageObject.
✅ Video Support – Add video tutorials with VideoObject, including content URL, embed URL, thumbnail, and duration.
✅ Course Mentions – Add related courses with links, descriptions, and provider info.
✅ Related Links – Include internal or external links as relatedLink for SEO and user navigation.
✅ JSON-LD Generator – Generates clean JSON-LD code ready to embed in your blog.
✅ Streamlit UI – User-friendly web interface for easy input and schema generation.

🔹 Installation

Clone the repository:

git clone https://github.com/yourusername/blog-schema-generator.git
cd blog-schema-generator


Install dependencies:

pip install streamlit


Run the app:

streamlit run app.py

🔹 Usage

Open the app in your browser (Streamlit will provide the URL).

Fill in blog details including headline, description, author, publisher, and keywords.

Add images with captions.

Add a video tutorial (optional).

Add related courses with URLs and descriptions.

Add related links (internal or external).

Click Generate JSON-LD Schema to view the generated schema.

Copy and embed the JSON-LD into your blog’s HTML <head> or before </body>.

🔹 Example Schema Output
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "Master Excel Formulas for Business Analytics",
  "description": "Learn the top Excel formulas every marketer and data analyst should know.",
  "author": {
    "@type": "Person",
    "name": "Siddharth",
    "url": "https://www.yourdomain.com/about"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Siddharth Computer Institute",
    "logo": {
      "@type": "ImageObject",
      "url": "https://www.yourdomain.com/images/logo.png"
    }
  },
  "datePublished": "2025-10-15",
  "dateModified": "2025-10-15",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://www.yourdomain.com/blog/excel-formulas"
  },
  "articleSection": "Education",
  "keywords": ["Excel Training", "Business Analytics", "Education", "Marketing Skills"],
  "image": [
    {
      "@type": "ImageObject",
      "url": "https://www.yourdomain.com/images/blog-excel-formulas-1.jpg",
      "caption": "Excel formulas dashboard example"
    }
  ],
  "video": {
    "@type": "VideoObject",
    "name": "Excel Formulas Tutorial Video",
    "description": "Step-by-step tutorial on key Excel formulas used in business analytics and marketing.",
    "thumbnailUrl": "https://www.yourdomain.com/images/excel-video-thumbnail.jpg",
    "uploadDate": "2025-10-15",
    "contentUrl": "https://www.yourdomain.com/videos/excel-formulas-tutorial.mp4",
    "embedUrl": "https://www.yourdomain.com/videos/embed/excel-formulas-tutorial",
    "duration": "PT5M30S"
  },
  "mentions": [
    {
      "@type": "Course",
      "name": "Microsoft Excel Training Course",
      "description": "Learn Excel from beginner to advanced level — formulas, dashboards, and automation with certification.",
      "provider": {
        "@type": "Organization",
        "name": "Siddharth Computer Institute",
        "sameAs": "https://www.yourdomain.com"
      },
      "url": "https://www.yourdomain.com/courses/excel-training"
    }
  ],
  "relatedLink": [
    "https://www.yourdomain.com/blog/power-bi-dashboard-tutorial"
  ]
}

🔹 Contributing

Contributions are welcome! You can:

Report bugs or issues

Suggest new features

Submit pull requests

Please follow standard GitHub contribution practices.

🔹 License

This project is licensed under the MIT License – see the LICENSE
 file for details.
