import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('data/DataCoSupplyChainDataset.csv', encoding = 'ISO-8859-1')
df.to_csv('data/SupplyChainETL.csv', encoding= 'utf-8', index = False)

engine = create_engine('sqlite:///SupplyChainETL.db')


customer_df = df[['Customer Id',
                  'Customer Fname',	
                  'Customer Lname',	
                  'Customer City',	
                  'Customer Country',
                  'Customer Street']].copy()

customer_df.columns = ['customer_id',
                       'customer_fname',
                       'customer_lname',
                       'customer_city',
                       'customer_country',
                       'customer_street'] 

customer_df = customer_df.drop_duplicates()
customer_df.to_sql('customer', con = engine, if_exists = 'append', index = False)


category_df = df[['Category Id',
                  'Category Name']].copy()

category_df.columns = ['category_id',
                       'category_name']

category_df = category_df.drop_duplicates()
category_df.to_sql('category', con = engine, if_exists = 'append', index = False)


item_df = df[['Product Card Id',
              'Product Category Id',	
              'Product Name',	
              'Product Price']].copy()

item_df.columns = [ 'product_id',
                    'product_category_id',
                    'product_name',
                    'product_price']

item_df = item_df.drop_duplicates(subset = 'product_id')
item_df.to_sql('item', con = engine, if_exists = 'append', index = False)


customer_order_df = df[['Order Id',
                        'Order Customer Id',
                        'order date (DateOrders)',
                        'Order Region',
                        'Order Status',
                        'Type']].copy()

customer_order_df.columns = ['order_id',
                             'order_customer_id',
                             'order_datetime',
                             'order_region',
                             'order_status',
                             'pay_type']

customer_order_df['order_datetime'] = pd.to_datetime(customer_order_df['order_datetime'])
customer_order_df = customer_order_df.drop_duplicates(subset = 'order_id')
customer_order_df.to_sql('customer_order', con = engine, if_exists = 'append', index = False)


order_item_df = df[['Order Item Id',
                    'Order Id',
                    'Order Item Cardprod Id',
                    'Order Item Product Price',
                    'Order Item Quantity',	
                    'Order Item Discount',
                    'Order Item Total']].copy()

order_item_df.columns = ['order_item_id',
                         'order_item_order_id',
                         'order_product_id',
                         'order_item_product_price',
                         'order_item_qty',
                         'order_item_discount',
                         'order_item_total']

order_item_df.to_sql('order_item', con = engine, if_exists = 'append', index = False)


delivery_detail_df = df[['Order Id',
                         'Days for shipping (real)',
                         'Days for shipment (scheduled)',
                         'Delivery Status',
                         'Late_delivery_risk',
                         'shipping date (DateOrders)',
                         'Shipping Mode']].copy()

delivery_detail_df.columns =['delivery_order_id',
                             'real_shipping_days',
                             'scheduled_shipping_days',
                             'delivery_status',
                             'late_delivery_risk',
                             'shipping_date',
                             'shipping_mode']

delivery_detail_df['shipping_date'] = pd.to_datetime(delivery_detail_df['shipping_date'])
delivery_detail_df = delivery_detail_df.drop_duplicates(subset = 'delivery_order_id') 
delivery_detail_df.to_sql('delivery_detail', con = engine, if_exists = 'append', index = False)