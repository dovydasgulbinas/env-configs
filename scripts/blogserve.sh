#!/bin/bash
echo "$BLOG_DIR"
cd $BLOG_DIR
bundle exec jekyll serve --drafts
