# Development
### Development setup

Install Hugo:
```bash
brew install hugo
```
Run the deveopment site
```bash
hugo server --watch --buildDrafts
```

### Deployment

#### Option 1: Manual deployment

Install Vercel (formerlly Zeit) `npm i -g vercel`

Run `vercel` to run an immutable deploy. You'll get a unique URL to the deploy.

Once happy, run `vercel --prod` to deploy behind http://dradrian.com

#### Option 2: CI

Anything on the master branch is automatically deployed to production.
