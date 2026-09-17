# DB2ADMIN.WRKBILLOFLADING

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 47
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 240314

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `BILLOFLADINGNO` | CHAR(20) |  |  |  |  |
| 5 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 6 | `BILLOFLADINGDATE` | DATE |  |  |  |  |
| 7 | `TOTALCONTAINERS` | INTEGER | NOT NULL |  |  |  |
| 8 | `GROSSWEIGHT` | DECIMAL(15,5) |  |  |  |  |
| 9 | `NETWEIGHT` | DECIMAL(15,5) |  |  |  |  |
| 10 | `WEIGHINGUOMCODE` | CHAR(3) |  |  |  |  |
| 11 | `DIVISIONNAME` | VARCHAR(200) |  |  |  |  |
| 12 | `INVOICENO` | CHAR(15) |  |  |  |  |
| 13 | `LCLCNO` | CHAR(35) |  |  |  |  |
| 14 | `GOODSORIGINCOUNTRYCODELD` | VARCHAR(200) |  |  |  |  |
| 15 | `TERMSOFSHIPPINGCODELD` | VARCHAR(200) |  |  |  |  |
| 16 | `PORTOFDISCHARGECODELD` | VARCHAR(200) |  |  |  |  |
| 17 | `PORTOFLOADINGCODELD` | VARCHAR(200) |  |  |  |  |
| 18 | `FINALDESTINATIONCODELD` | VARCHAR(200) |  |  |  |  |
| 19 | `CONSIGNEELEGALNAME1` | VARCHAR(270) |  |  |  |  |
| 20 | `NOTIFYLEGALNAME1` | VARCHAR(270) |  |  |  |  |
| 21 | `COUNTRYCODE` | CHAR(3) |  |  |  |  |
| 22 | `NOTIFYCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 23 | `ADDRESSLINE1` | VARCHAR(150) |  |  |  |  |
| 24 | `NOTIFYADDRESSLINE1` | VARCHAR(150) |  |  |  |  |
| 25 | `ADDRESSLINE2` | VARCHAR(150) |  |  |  |  |
| 26 | `NOTIFYADDRESSLINE2` | VARCHAR(150) |  |  |  |  |
| 27 | `ADDRESSLINE3` | VARCHAR(150) |  |  |  |  |
| 28 | `NOTIFYADDRESSLINE3` | VARCHAR(150) |  |  |  |  |
| 29 | `ADDRESSLINE5` | VARCHAR(150) |  |  |  |  |
| 30 | `NOTIFYADDRESSLINE5` | VARCHAR(150) |  |  |  |  |
| 31 | `ADDRESSLINE4` | VARCHAR(150) |  |  |  |  |
| 32 | `NOTIFYADDRESSLINE4` | VARCHAR(150) |  |  |  |  |
| 33 | `POSTALCODE` | CHAR(20) |  |  |  |  |
| 34 | `NOTIFYPOSTALCODE` | CHAR(20) |  |  |  |  |
| 35 | `TOWN` | VARCHAR(200) |  |  |  |  |
| 36 | `NOTIFYTOWN` | VARCHAR(200) |  |  |  |  |
| 37 | `DISTRICT` | VARCHAR(200) |  |  |  |  |
| 38 | `NOTIFYDISTRICT` | VARCHAR(200) |  |  |  |  |
| 39 | `TRANSPORTZONECODE` | CHAR(3) |  |  |  |  |
| 40 | `NOTIFYTRANSPORTZONECODE` | CHAR(3) |  |  |  |  |
| 41 | `ADDRESSPHONENUMBER` | VARCHAR(80) |  |  |  |  |
| 42 | `NOTIFYADDRESSPHONENUMBER` | VARCHAR(80) |  |  |  |  |
| 43 | `ADDRESSFAXNUMBER` | VARCHAR(80) |  |  |  |  |
| 44 | `NOTIFYADDRESSFAXNUMBER` | VARCHAR(80) |  |  |  |  |
| 45 | `PLANTINVOICELRNO` | CHAR(15) |  |  |  |  |
| 46 | `SHIPPINGMARK` | VARCHAR(1000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.COMPANYCODE,
       t.BILLOFLADINGNO,
       t.DIVISIONCODE,
       t.BILLOFLADINGDATE,
       t.TOTALCONTAINERS,
       t.GROSSWEIGHT,
       t.NETWEIGHT,
       t.WEIGHINGUOMCODE,
       t.DIVISIONNAME
FROM   DB2ADMIN.WRKBILLOFLADING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
