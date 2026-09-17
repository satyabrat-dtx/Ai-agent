# DB2ADMIN.WRKSALESORDERREPORT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 51
- **Primary key**: `CREATIONTIMESTAMP`, `CREATIONUSER`, `COMPANYCODE`, `SALESORDERCOUNTERCODE`, `SALESORDERCODE`, `ORDERLINE`, `ORDERSUBLINE`, `COMPONENTORDERLINE`, `DELIVERYLINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 146164

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) | NOT NULL | PK | primary_key audit | User who created the row (audit). |
| 2 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `SALESORDERCOUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 4 | `SALESORDERCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 5 | `ORDERLINE` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 6 | `ORDERSUBLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 7 | `COMPONENTORDERLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 8 | `DELIVERYLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 9 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 10 | `ORDERDATE` | DATE | NOT NULL |  |  |  |
| 11 | `ORDERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 12 | `CUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 13 | `CUSTOMERCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 14 | `CUSTOMERCOUNRYDESC` | VARCHAR(200) |  |  |  |  |
| 15 | `CUSTOMERTRANSPORTZONECODE` | CHAR(3) |  |  |  |  |
| 16 | `CUSTOMERTRANSPORTZONEDESC` | VARCHAR(200) |  |  |  |  |
| 17 | `BUSSINESSPARTNERNUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 18 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 19 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 20 | `STYLE` | VARCHAR(200) |  |  |  |  |
| 21 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 22 | `TERMSOFDELIVERYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 23 | `TERMSOFSHIPPINGCODE` | CHAR(3) |  |  |  |  |
| 24 | `TERMSOFSHIPPINGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 25 | `FIRSTCARRIERLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 26 | `SECONDCARRIERLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 27 | `THIRDCARRIERLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 28 | `ORDERDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 29 | `BUSINESSGROUPCODE` | CHAR(6) |  |  |  |  |
| 30 | `BUSINESSGROUPDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 31 | `AGENTCODE` | CHAR(3) |  |  |  |  |
| 32 | `AGENTDESC` | VARCHAR(200) |  |  |  |  |
| 33 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 34 | `INTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 35 | `PRODUCTCODE` | VARCHAR(200) |  |  |  |  |
| 36 | `PRODUCTDESC` | VARCHAR(200) |  |  |  |  |
| 37 | `SECONDARYSUBCODES` | VARCHAR(200) |  |  |  |  |
| 38 | `DELIVERYQTY` | DECIMAL(15,5) |  |  |  |  |
| 39 | `QTYUOMCODE` | CHAR(3) |  |  |  |  |
| 40 | `SOLINECOMMENT` | VARCHAR(200) |  |  |  |  |
| 41 | `SOCOMMENT` | VARCHAR(200) |  |  |  |  |
| 42 | `SONOTE` | CHAR(100) |  |  |  |  |
| 43 | `MERCHANGENAME` | CHAR(50) |  |  |  |  |
| 44 | `LIGHTSOURCE` | CHAR(50) |  |  |  |  |
| 45 | `ENDBUYER` | CHAR(50) |  |  |  |  |
| 46 | `CUSTOMERPO` | VARCHAR(200) |  |  |  |  |
| 47 | `DELIVERYDATE` | DATE |  |  |  |  |
| 48 | `TYPEOFINVOICE` | CHAR(30) |  |  |  |  |
| 49 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 50 | `APPROVEDOPTION` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.COMPANYCODE,
       t.SALESORDERCOUNTERCODE,
       t.SALESORDERCODE,
       t.ORDERLINE,
       t.ORDERSUBLINE,
       t.COMPONENTORDERLINE,
       t.DELIVERYLINE,
       t.DIVISIONCODE,
       t.ORDERDATE,
       t.ORDERTYPE
FROM   DB2ADMIN.WRKSALESORDERREPORT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
