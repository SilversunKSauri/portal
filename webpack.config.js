// webpack plugins
const CommonsChunkPlugin = require('webpack/lib/optimize/CommonsChunkPlugin');
const webpack = require('webpack');
const path = require('path');
const ngAnnotatePlugin = require('ng-annotate-webpack-plugin');
const LiveReloadPlugin = require('webpack-livereload-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  devtool: 'source-map',
  entry: './designsafe/apps/geo/static/designsafe/apps/geo/scripts/index.js',
  output: {
    path: __dirname,
    filename: "./designsafe/apps/geo/static/designsafe/apps/geo/build/bundle.[hash].js"
  },
  resolve: {
    extensions: ['.js'],
    modules: ['node_modules']
  },

  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
        options: {
          presets: ['es2015']
        }
      },
      {test: /\.css$/, use: 'css-loader'},
    ]
  },
  plugins: [
    new ngAnnotatePlugin({add:true}),

    new LiveReloadPlugin(),

  ],

  externals: {
    jQuery: 'jQuery',
    $: 'jQuery',
    jquery: 'jQuery',
    Modernizr: 'Modernizr',
    angular: 'angular',
    d3: 'd3',
    moment: 'moment',
    _: '_',
    L: 'L',
    window: 'window',
  }
};