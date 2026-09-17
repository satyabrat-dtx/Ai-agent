# DB2ADMIN.WRKCOMPARATIVESTMT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 40
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 109374

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CHOOSE` | SMALLINT | NOT NULL |  |  |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `RFQHEADERRFQHEADERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 4 | `RFQHEADERRFQHEADERCODE` | CHAR(15) |  |  |  |  |
| 5 | `RFQHEADERLINENO` | INTEGER | NOT NULL |  |  |  |
| 6 | `ORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 7 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 8 | `SUPPLIERDESC` | VARCHAR(200) |  |  |  |  |
| 9 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 10 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 11 | `FULLITEM` | CHAR(140) |  |  |  |  |
| 12 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 13 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 14 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 17 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 23 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 24 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 25 | `UOMCODE` | CHAR(3) |  |  |  |  |
| 26 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 27 | `GROSSPRICE` | DECIMAL(18,5) |  |  |  |  |
| 28 | `PRICEUOMCODE` | CHAR(3) |  |  |  |  |
| 29 | `DELIVERYDATE` | DATE |  |  |  |  |
| 30 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 31 | `QUOTEVALIDTILL` | DATE |  |  |  |  |
| 32 | `MINBASEPRICE` | SMALLINT | NOT NULL |  |  |  |
| 33 | `MINGROSSPRICE` | SMALLINT | NOT NULL |  |  |  |
| 34 | `EARLIESTDELVDATE` | SMALLINT | NOT NULL |  |  |  |
| 35 | `SECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 36 | `SECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 37 | `PACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 38 | `PACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 39 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKCOMPARATIVESTMTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CHOOSE,
       t.COMPANYCODE,
       t.DIVISIONCODE,
       t.RFQHEADERRFQHEADERCOUNTERCODE,
       t.RFQHEADERRFQHEADERCODE,
       t.RFQHEADERLINENO,
       t.ORDPRNCUSTOMERSUPPLIERTYPE,
       t.ORDPRNCUSTOMERSUPPLIERCODE,
       t.SUPPLIERDESC,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.FULLITEM
FROM   DB2ADMIN.WRKCOMPARATIVESTMT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
