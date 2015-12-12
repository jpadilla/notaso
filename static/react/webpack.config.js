var path = require('path');

module.exports = {
  entry: {
    app: ['./app.js']
  },
  output: {
    path: path.resolve(__dirname, 'build'),
    publicPath: '/',
    filename: 'bundle.js'
  },
  module: {
    loaders: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: 'babel?presets[]=es2015&presets[]=react&presets[]=stage-0'
      }
    ]
  }
};
