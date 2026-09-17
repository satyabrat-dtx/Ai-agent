# DB2ADMIN.WRKBANKINGCOVER

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 49
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `DIVISIONCODE`, `BOECODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 144217

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 3 | `BOECODE` | CHAR(12) | NOT NULL | PK | primary_key |  |
| 4 | `BOEDATE` | DATE |  |  |  |  |
| 5 | `EXPBANKLONGDESP` | VARCHAR(200) |  |  |  |  |
| 6 | `ADDRESSLINE1` | VARCHAR(200) |  |  |  |  |
| 7 | `ADDRESSLINE2` | VARCHAR(200) |  |  |  |  |
| 8 | `ADDRESSLINE3` | VARCHAR(200) |  |  |  |  |
| 9 | `ADDRESSLINE4` | VARCHAR(200) |  |  |  |  |
| 10 | `ADDRESSLINE5` | VARCHAR(200) |  |  |  |  |
| 11 | `POSTALCODE` | CHAR(20) |  |  |  |  |
| 12 | `TOWN` | VARCHAR(200) |  |  |  |  |
| 13 | `DISTRICT` | VARCHAR(200) |  |  |  |  |
| 14 | `COUNTRYNAME` | VARCHAR(200) |  |  |  |  |
| 15 | `PURCHASEORDERNO` | VARCHAR(200) |  |  |  |  |
| 16 | `DESCRIPTION1` | CHAR(50) |  |  |  |  |
| 17 | `ORIGINAL1` | DECIMAL(7,0) |  |  |  |  |
| 18 | `COPY1` | DECIMAL(7,0) |  |  |  |  |
| 19 | `DESCRIPTION2` | CHAR(50) |  |  |  |  |
| 20 | `ORIGINAL2` | DECIMAL(7,0) |  |  |  |  |
| 21 | `COPY2` | DECIMAL(7,0) |  |  |  |  |
| 22 | `DESCRIPTION3` | CHAR(50) |  |  |  |  |
| 23 | `ORIGINAL3` | DECIMAL(7,0) |  |  |  |  |
| 24 | `COPY3` | DECIMAL(7,0) |  |  |  |  |
| 25 | `FIRMBANKLONGDESP` | VARCHAR(200) |  |  |  |  |
| 26 | `FIRMADDRESSLINE1` | VARCHAR(200) |  |  |  |  |
| 27 | `FIRMADDRESSLINE2` | VARCHAR(200) |  |  |  |  |
| 28 | `FIRMADDRESSLINE3` | VARCHAR(200) |  |  |  |  |
| 29 | `FIRMADDRESSLINE4` | VARCHAR(200) |  |  |  |  |
| 30 | `FIRMADDRESSLINE5` | VARCHAR(200) |  |  |  |  |
| 31 | `FIRMPOSTALCODE` | CHAR(20) |  |  |  |  |
| 32 | `FIRMTOWN` | VARCHAR(200) |  |  |  |  |
| 33 | `FIRMDISTRICT` | VARCHAR(200) |  |  |  |  |
| 34 | `FIRMCOUNTRYNAME` | VARCHAR(200) |  |  |  |  |
| 35 | `EXPSHIPPINGBILLNO` | CHAR(12) |  |  |  |  |
| 36 | `EXPSHIPPINGDATE` | DATE |  |  |  |  |
| 37 | `COMMERCIALINVOICECODE` | VARCHAR(1000) |  |  |  |  |
| 38 | `SHIPNOANDDATE` | VARCHAR(1000) |  |  |  |  |
| 39 | `BLAWBNO` | VARCHAR(1000) |  |  |  |  |
| 40 | `COMMAMOUNT` | VARCHAR(1000) |  |  |  |  |
| 41 | `ROLEINTHECOMPANY` | VARCHAR(200) |  |  |  |  |
| 42 | `COMMINVANDDATE` | VARCHAR(1000) |  |  |  |  |
| 43 | `AWBNOANDDATE` | VARCHAR(1000) |  |  |  |  |
| 44 | `INVAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 45 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 46 | `LCNO` | CHAR(35) |  |  |  |  |
| 47 | `LCDATE` | DATE |  |  |  |  |
| 48 | `LINENO` | BIGINT | NOT NULL | PK | primary_key |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.DIVISIONCODE,
       t.BOECODE,
       t.BOEDATE,
       t.EXPBANKLONGDESP,
       t.ADDRESSLINE1,
       t.ADDRESSLINE2,
       t.ADDRESSLINE3,
       t.ADDRESSLINE4,
       t.ADDRESSLINE5,
       t.POSTALCODE
FROM   DB2ADMIN.WRKBANKINGCOVER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
