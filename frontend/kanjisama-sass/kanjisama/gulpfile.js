'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass');
var clean = require('gulp-clean');
var livereload = require('gulp-livereload');
var concat = require('gulp-concat');

gulp.task('clean', function() {
    return gulp.src('./css/app.css', {read: false})
        .pipe(clean());
});

gulp.task('sass', function () {
    return gulp.src('./sass/app.scss')
        .pipe(sass({outputStyle: 'expanded'}).on('error', sass.logError))
        .pipe(gulp.dest('./css'))
        .pipe(livereload());
});

gulp.task('watch', function() {
    livereload.listen();
    gulp.watch('./sass/*.sass', ['sass']);
});

gulp.task('default', ['clean', 'sass']);
