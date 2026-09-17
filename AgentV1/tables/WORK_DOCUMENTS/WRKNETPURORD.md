# DB2ADMIN.WRKNETPURORD

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 79
- **Primary key**: `CREATIONTIMESTAMP`, `LINENO`, `COMPANYCODE`, `COUNTERCODE`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 240043

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `COUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 4 | `CODE` | CHAR(15) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 5 | `COMPANYDES` | VARCHAR(250) |  |  |  |  |
| 6 | `ADDRESSLINE1` | VARCHAR(250) |  |  |  |  |
| 7 | `ADDRESSLINE2` | VARCHAR(250) |  |  |  |  |
| 8 | `ADDRESSLINE3` | VARCHAR(250) |  |  |  |  |
| 9 | `COUNTRYCODE` | VARCHAR(250) |  |  |  |  |
| 10 | `ADDRESSPHONENUMBER` | VARCHAR(250) |  |  |  |  |
| 11 | `EMAILADDRESS` | VARCHAR(250) |  |  |  |  |
| 12 | `ADDRESSLINE4` | VARCHAR(250) |  |  |  |  |
| 13 | `ADDRESSGST` | VARCHAR(250) |  |  |  |  |
| 14 | `SUPPLIERNAME` | VARCHAR(250) |  |  |  |  |
| 15 | `SUPADD1` | VARCHAR(250) |  |  |  |  |
| 16 | `SUPADD2` | VARCHAR(250) |  |  |  |  |
| 17 | `SUPCOUTRY` | VARCHAR(250) |  |  |  |  |
| 18 | `SUPADDGST` | CHAR(15) |  |  |  |  |
| 19 | `ORDERDATE` | DATE |  |  |  |  |
| 20 | `POTYPE` | VARCHAR(250) |  |  |  |  |
| 21 | `TERMSOFPAYMENT` | VARCHAR(250) |  |  |  |  |
| 22 | `TERMSOFDELIVERY` | VARCHAR(250) |  |  |  |  |
| 23 | `TERMSOFSHIPPING` | VARCHAR(250) |  |  |  |  |
| 24 | `ORDERLINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 25 | `ORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 26 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 27 | `ITEMDESCRIPTION` | VARCHAR(250) |  |  |  |  |
| 28 | `TARIFFCODEHSN` | VARCHAR(250) |  |  |  |  |
| 29 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 30 | `UOM` | VARCHAR(250) |  |  |  |  |
| 31 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 32 | `CURRENCY` | VARCHAR(250) |  |  |  |  |
| 33 | `AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 34 | `WFMORDERSTATUS` | INTEGER | NOT NULL |  |  |  |
| 35 | `WFMSTATUS` | VARCHAR(250) |  |  |  |  |
| 36 | `APPROVEDBY` | VARCHAR(250) |  |  |  |  |
| 37 | `APPROVEDDATE` | TIMESTAMP |  |  |  |  |
| 38 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 39 | `COMMENT` | VARCHAR(250) |  |  |  |  |
| 40 | `PURLINEABSUNIQUE` | BIGINT | NOT NULL |  |  |  |
| 41 | `COMMENTCODE` | CHAR(12) |  |  |  |  |
| 42 | `DELIVERYAD1` | VARCHAR(250) |  |  |  |  |
| 43 | `DELADDLINE1` | VARCHAR(250) |  |  |  |  |
| 44 | `DELADDLINE2` | VARCHAR(250) |  |  |  |  |
| 45 | `DELADDLINE3` | VARCHAR(250) |  |  |  |  |
| 46 | `DELTOWN` | VARCHAR(250) |  |  |  |  |
| 47 | `DELDISTRICT` | VARCHAR(250) |  |  |  |  |
| 48 | `DELPOSTALCODE` | VARCHAR(250) |  |  |  |  |
| 49 | `DELADDPHNNUM` | VARCHAR(250) |  |  |  |  |
| 50 | `DELEMAIL` | VARCHAR(250) |  |  |  |  |
| 51 | `DELECOUNTRY` | VARCHAR(250) |  |  |  |  |
| 52 | `ITEMCODE` | VARCHAR(250) |  |  |  |  |
| 53 | `PURHDRABSUNIQUE` | BIGINT | NOT NULL |  |  |  |
| 54 | `LINEAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 55 | `HDRAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 56 | `WFMLOGIC` | VARCHAR(250) |  |  |  |  |
| 57 | `IEHDRGROSS` | DECIMAL(18,5) |  |  |  |  |
| 58 | `IELNGROSS` | DECIMAL(18,5) |  |  |  |  |
| 59 | `DELIDATE` | DATE |  |  |  |  |
| 60 | `ADDRESSLINE5` | VARCHAR(250) |  |  |  |  |
| 61 | `ADDRESSEE` | VARCHAR(250) |  |  |  |  |
| 62 | `ADDRESSEE2` | VARCHAR(250) |  |  |  |  |
| 63 | `POSTALCODE` | VARCHAR(250) |  |  |  |  |
| 64 | `TOWN` | VARCHAR(250) |  |  |  |  |
| 65 | `DISTRICT` | VARCHAR(250) |  |  |  |  |
| 66 | `SUPADD3` | VARCHAR(250) |  |  |  |  |
| 67 | `SUPADD4` | VARCHAR(250) |  |  |  |  |
| 68 | `SUPADD5` | VARCHAR(250) |  |  |  |  |
| 69 | `SUPADDRESSEE` | VARCHAR(250) |  |  |  |  |
| 70 | `SUPADDRESSEE2` | VARCHAR(250) |  |  |  |  |
| 71 | `SUPTOWN` | VARCHAR(250) |  |  |  |  |
| 72 | `SUPDISTRICT` | VARCHAR(250) |  |  |  |  |
| 73 | `SUPADDPHNNUM` | VARCHAR(250) |  |  |  |  |
| 74 | `SUPEMAIL` | VARCHAR(250) |  |  |  |  |
| 75 | `SUPPOSTALCODE` | VARCHAR(250) |  |  |  |  |
| 76 | `DELADDLINE4` | VARCHAR(250) |  |  |  |  |
| 77 | `DELADDLINE5` | VARCHAR(250) |  |  |  |  |
| 78 | `DELIGSTCODE` | VARCHAR(250) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.LINENO,
       t.COMPANYCODE,
       t.COUNTERCODE,
       t.CODE,
       t.COMPANYDES,
       t.ADDRESSLINE1,
       t.ADDRESSLINE2,
       t.ADDRESSLINE3,
       t.COUNTRYCODE,
       t.ADDRESSPHONENUMBER,
       t.EMAILADDRESS
FROM   DB2ADMIN.WRKNETPURORD t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
