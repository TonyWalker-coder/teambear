# TeamBear

## Table of Contents

- [User Stories](#userstory)
- [Intellectual Property & Educational Use](#ip)
- [Image store and handling](#imagestore)


- [Browser Support](#browsersupport)


<a id="userstory"></a>

## User Stories
 
### Introduction
 
The purpose of TeamBear is to provide an e-commerce platform for selling bespoke teddy bears. The application is designed to allow customers to easily browse products, view detailed information, and complete purchases through a secure and intuitive interface.
 
By focusing on usability, accessibility, and customer satisfaction, the site aims to encourage repeat

## Accessibility
 
### User Story
 
As a site owner, I want the website to be accessible and responsive so that all users can navigate and interact with the site regardless of device, browser, or assistive technology.
 
### Acceptance Criteria
 
#### Accessibility
 
- All form inputs must have associated `<label>` elements.
- All interactive elements must be fully keyboard accessible.
- Screen readers must be able to identify the purpose of all controls and content.
- Colour contrast must meet WCAG AA accessibility standards.
- Appropriate semantic HTML must be used throughout the site.
- ARIA attributes must be used where required to improve accessibility.
 
#### Responsiveness
 
- The site must be fully responsive across desktop, tablet, and mobile devices.
- Users should be able to access the same functionality regardless of platform.
- Navigation and layout should remain intuitive across all screen sizes.
 
#### Consistency
 
- Styling must remain consistent across all pages.
- The homepage should establish the visual theme used throughout the site.
- The navigation bar should remain visible and easily accessible throughout the user journey.
 
### Tasks
 
- [ ] Create a light/dark theme.
- [ ] Define design tokens in `styles.css`.
- [ ] Create a fixed header/navigation bar.
- [ ] Ensure full keyboard navigation.
- [ ] Test compatibility with screen readers.
- [ ] Implement ARIA labels where appropriate.
- [ ] Validate colour contrast against WCAG AA standards.
- [ ] Test responsiveness across desktop, tablet, and mobile devices.

## Homepage
 
### User Story
 
As a site owner, I want the homepage to present the TeamBear brand in a clear and professional manner so that visitors immediately understand the products we sell and feel encouraged to explore the website.
 
### Acceptance Criteria
 
- The site must have a dedicated homepage that serves as the main entry point for visitors.
- The homepage must clearly communicate the purpose of the site and the products available.
- A prominent hero section must showcase the TeamBear brand and product range.
- The visual theme established on the homepage must remain consistent throughout the site.
- The homepage must provide clear navigation to key areas of the website.
- The layout must remain visually appealing and functional on desktop, tablet, and mobile devices.
 
### Tasks
 
- [ ] Create a homepage template.
- [ ] Include a themed hero image or banner.
- [ ] Add a clear heading and introductory message.
- [ ] Create call-to-action buttons linking to products.
- [ ] Ensure the hero image scales appropriately across screen sizes.
- [ ] Maintain branding and styling consistency throughout the site.
- [ ] Test responsiveness on desktop, tablet, and mobile devices.


## Navigation
 
### User Story
 
As a visitor, I want to navigate the site intuitively and efficiently so that I can quickly access the information and features I need.
 
### Acceptance Criteria
 
- A navigation bar is displayed on every page of the website.
- The navigation bar remains consistent in appearance and functionality across all pages.
- Navigation links allow users to move easily between key sections of the site.
- The navigation menu is fully responsive and accessible on smaller screen sizes.
 
### Tasks
 
- [ ] Create a reusable navbar template.
- [ ]  Implement a responsive mobile navigation menu.
- [ ]  Attach the navbar to a fixed header for persistent access during scrolling.
- [ ]  Ensure navigation links are consistent across all pages.
- [ ]  Test navbar functionality on desktop, tablet, and mobile devices.

## Product range
 
### User Story
 
As a visitor, I want to search and browse the product range so that I can quickly find products that match my interests and view my selected results in one place.
 
### Acceptance Criteria
 
- Products can be filtered and searched using multiple categories.
- Search results are displayed in a responsive grid layout.
- Each product is presented within a consistent product card.
- Product cards display all relevant product information, including name, image, category, and description.
- A fallback image is displayed when a product image is unavailable.
 
### Tasks
 
- [ ] Create product search and filtering functionality.
- [ ]  Implement category-based filtering options.
- [ ]  Design and build a reusable product card component.
- [ ]  Display all relevant product information within each card.
- [ ]  Create and implement a standard fallback image.
- [ ]  Develop a responsive grid layout for product display.
- [ ]  Test search and filtering functionality across different devices.

## Product selection
 
### User Story
 
As a visitor, I want to select products I wish to purchase so that I can add them to my shopping basket and manage the quantity before checkout.
 
### Acceptance Criteria
 
- Product cards are clickable and allow users to view or select a product.
- Users can choose the quantity of a selected product.
- Selected products are added to the shopping basket.
- The shopping basket updates automatically when products are added.
- Users receive clear visual feedback confirming that a product has been added to the basket.
 
### Tasks
 
- [ ] Make product cards clickable.
- [ ] Create a product detail or selection view.
- [ ] Implement a quantity selector.
- [ ] Add functionality to add products to the shopping basket.
- [ ] Display a confirmation message when a product is added.
- [ ] Update basket totals and item counts dynamically.
- [ ] Test product selection and basket functionality across different devices.

## Shopping basket
 
### User Story
 
As a visitor, I want to view the products I have selected, along with their quantities and total cost, so that I can review my order before proceeding to checkout.
 
### Acceptance Criteria
 
- The shopping basket displays all selected products.
- ach basket item shows the product name, quantity, and individual price.
- The subtotal for each product is calculated based on the item price multiplied by the selected quantity.
- The basket displays the overall total cost of all selected products.
- Basket contents update automatically when products are added, removed, or quantities are changed.
 
### Tasks
 
- [ ] Create a shopping basket view.
- [ ] Display selected products within the basket.
- [ ] Track and display individual product prices.
- [ ] Calculate and display item subtotals.
- [ ] Calculate and display the basket total.
- [ ] Implement functionality to update item quantities.
- [ ] Implement functionality to remove products from the basket.
- [ ] Test basket calculations and updates across different devices.


## Secure payment
 
### User Story
 
As a visitor, I want my payment information to be handled securely so that I can complete my purchase with confidence.
 
### Acceptance Criteria
 
- A dedicated checkout page is provided for processing orders.
- The checkout form collects all information required to complete a purchase.
- Payments are processed through a secure third-party payment provider.
- Sensitive payment information is not stored within the application.
- Users receive clear confirmation when a payment is successful.
- Users are informed if a payment fails and are given the opportunity to try again.
- Customers can choose to receive an order confirmation email.
 
### Tasks
 
- [ ] Create a dedicated checkout page.
- [ ] Integrate Stripe as the payment processor.
- [ ] Validate customer and payment information before submission.
- [ ] Secure all API keys and sensitive configuration variables using environment variables.
- [ ] Implement payment success and failure handling.
- [ ] Display transaction status messages to users.
- [ ] Generate and store order records following successful payments.
- [ ] Send an order confirmation email when requested.
- [ ] Test payment workflows using Stripe test payments.

## User Registration

### User Story

As a visitor, I want to create an account so that I can access my order history, receive member benefits, and enjoy a more personalised shopping experience.

### Acceptance Criteria

- Visitors can register for an account using a valid email address and password.
- Registered users can securely log in and log out.
- Registered users can view their previous orders.
- Registered users can access any available member discounts or special offers.
- Users receive confirmation when registration is successful.
- User account information is stored securely.

### Tasks

- [ ] Create a user registration form.
- [ ] Create a login and logout system.
- [ ] Validate registration data and password requirements.
- [ ] Store user information securely.
- [ ] Create an account dashboard page.
- [ ] Display previous orders on the user dashboard.
- [ ] Implement member discount functionality.
- [ ] Display registration and authentication messages.
- [ ] Test registration, login, and account management features.

## Order History

## Product Maintenance

### User Story

As a site owner, I want additional product management options to be available when I am logged in so that I can quickly update products without leaving the main site interface.

### Acceptance Criteria

- Product management controls are only visible to authorised site owners.
- Regular users cannot see or access management controls.
- Site owners can update product prices.
- Site owners can update stock levels.
- Site owners can mark products as special offers.
- Changes are saved and reflected immediately on the site.

### Tasks

- [ ] Restrict management features to authorised users.
- [ ] Display edit controls conditionally based on user permissions.
- [ ] Implement price editing functionality.
- [ ] Implement stock level editing functionality.
- [ ] Implement a special offer toggle.
- [ ] Display confirmation messages when changes are saved.
- [ ] Test role-based access and permissions.

<a id="ip"></a>

## Intellectual Property & Educational Use

This project was created solely for educational and portfolio purposes as part of a software development programme.
 
Football-related imagery, colours, and designs have been used to demonstrate the functionality of the application. Any club names, crests, kit designs, sponsor references, or other trademarks remain the property of their respective owners.
 
This project is not affiliated with, endorsed by, sponsored by, or associated with any football club, league, manufacturer, or sponsor.
 
The website is non-commercial and has been developed exclusively for educational assessment purposes.

## Site Footer Disclaimer

Educational Project Disclaimer
 
This website is an Educational Project • Non-Commercial Use • No Affiliation with Any Football Club or Brand

<a id="imagestore"></a>

### Image store and handling

A source image store was maintained during development containing original PNG assets. Optimised WebP versions were generated from these originals for deployment. This allowed assets to be modified and regenerated throughout testing without cumulative quality loss. Once testing was complete and the final optimised images were produced, the original working assets were removed from the deployed project.


