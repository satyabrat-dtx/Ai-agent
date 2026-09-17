# DB2ADMIN.WRKNETEXTOPDOCUMENT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 54
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 239683

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `CUSER` | CHAR(50) |  |  |  |  |
| 4 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 5 | `DEFINITIVECODE` | CHAR(15) |  |  |  |  |
| 6 | `DOCCOUNTERCODE` | CHAR(15) |  |  |  |  |
| 7 | `FIRSTCARRIERCODE` | CHAR(15) |  |  |  |  |
| 8 | `PROVCOUNTERCODE` | CHAR(15) |  |  |  |  |
| 9 | `SUPPLIERCODE` | CHAR(15) |  |  |  |  |
| 10 | `TERMSOFDELIVERYLD` | VARCHAR(200) |  |  |  |  |
| 11 | `DOCCODE` | CHAR(15) |  |  |  |  |
| 12 | `PROVISIONALCODE` | CHAR(15) |  |  |  |  |
| 13 | `TERMSOFSHIPPINGLD` | VARCHAR(200) |  |  |  |  |
| 14 | `COMPANYLD` | VARCHAR(200) |  |  |  |  |
| 15 | `DOCDOCUMENTDATE` | DATE |  |  |  |  |
| 16 | `PROVISIONALDOCUMENTDATE` | DATE |  |  |  |  |
| 17 | `DIVISIONNAME` | VARCHAR(200) |  |  |  |  |
| 18 | `ADDRESSEE` | VARCHAR(200) |  |  |  |  |
| 19 | `ADDRESSEE2` | VARCHAR(200) |  |  |  |  |
| 20 | `ADDRESSLINE1` | VARCHAR(150) |  |  |  |  |
| 21 | `CADDRESSLINE1` | VARCHAR(150) |  |  |  |  |
| 22 | `ADDRESSLINE2` | VARCHAR(150) |  |  |  |  |
| 23 | `CADDRESSLINE2` | VARCHAR(150) |  |  |  |  |
| 24 | `ADDRESSLINE3` | VARCHAR(150) |  |  |  |  |
| 25 | `CADDRESSLINE3` | VARCHAR(150) |  |  |  |  |
| 26 | `ADDRESSLINE4` | VARCHAR(150) |  |  |  |  |
| 27 | `DEFINITIVEDOCUMENTDATE` | DATE |  |  |  |  |
| 28 | `CADDRESSLINE4` | VARCHAR(150) |  |  |  |  |
| 29 | `ADDRESSLINE5` | VARCHAR(150) |  |  |  |  |
| 30 | `ADDRESSFAXNUMBER` | VARCHAR(200) |  |  |  |  |
| 31 | `BADDRESSFAXNUMBER` | VARCHAR(200) |  |  |  |  |
| 32 | `CADDRESSLINE5` | VARCHAR(150) |  |  |  |  |
| 33 | `CPOSTALCODE` | CHAR(20) |  |  |  |  |
| 34 | `POSTALCODE` | CHAR(20) |  |  |  |  |
| 35 | `CTOWN` | VARCHAR(200) |  |  |  |  |
| 36 | `CADDRESSPHONENUMBER` | VARCHAR(80) |  |  |  |  |
| 37 | `TOWN` | VARCHAR(200) |  |  |  |  |
| 38 | `ADDRESSPHONENUMBER` | VARCHAR(80) |  |  |  |  |
| 39 | `CONSIGNEELEGALNAME1` | VARCHAR(270) |  |  |  |  |
| 40 | `BASICVALUE` | DECIMAL(18,5) |  |  |  |  |
| 41 | `EXTITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 42 | `ITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 43 | `GSTINNUMBER` | CHAR(15) |  |  |  |  |
| 44 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 45 | `EXTERNOPLINECOUNTERCODE` | CHAR(3) |  |  |  |  |
| 46 | `FACTORYGSTINNUMBER` | CHAR(15) |  |  |  |  |
| 47 | `EXTERNOPLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 48 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 49 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 50 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 51 | `TARIFFCODE` | CHAR(20) |  |  |  |  |
| 52 | `BUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 53 | `EXTERNOPLINECODE` | CHAR(15) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.CUSER,
       t.COMPANYCODE,
       t.DEFINITIVECODE,
       t.DOCCOUNTERCODE,
       t.FIRSTCARRIERCODE,
       t.PROVCOUNTERCODE,
       t.SUPPLIERCODE,
       t.TERMSOFDELIVERYLD,
       t.DOCCODE
FROM   DB2ADMIN.WRKNETEXTOPDOCUMENT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
