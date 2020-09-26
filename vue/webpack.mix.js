let mix = require('laravel-mix');   
const webpack = require('webpack');
const CompressionPlugin = require('compression-webpack-plugin');
const tailwindcss = require('tailwindcss')

mix.js('src/js/app.js', 'public/js/app.js')
   .sass('src/sass/style.scss', 'public/css',{
        'sassOptions':{
            includePaths:[
            'node_modules/normalize-scss/sass'
            ]
        }
        
    })
    .options({
        processCssUrls: false,
        postCss: [ tailwindcss('tailwind.config.js') ],
      })
   .webpackConfig({
        mode: 'production',
        devtool: "cheap-module-source-map",     // "eval-source-map" or "inline-source-map" or "cheap-module-source-map" or "eval"
        plugins: [
            new CompressionPlugin({             // very import to compress the assets
                filename: "[path].gz[query]",
                algorithm: "gzip",
                test: /\.js$|\.css$|\.html$|\.svg$/,
                threshold: 10240,
                minRatio: 0.8
            }),
            new webpack.IgnorePlugin(/^\.\/locale$/, /moment$/)
        ],
        output: {
            chunkFilename: '[name].js?id=[chunkhash]',
        },
    });
if (mix.inProduction()) {                       // In production environtment use versioning
    //mix.version();
}