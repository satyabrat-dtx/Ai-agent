# DB2ADMIN.ITEMSHEETWORK

- **Module**: `ITEM_MASTER` (high confidence — table name starts with 'ITEM')
- **Roles**: `business_data`
- **Columns**: 33
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 35398

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(8) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `COST` | DECIMAL(18,5) |  |  |  |  |
| 2 | `COSTTYPE` | CHAR(2) |  |  |  |  |
| 3 | `TYPE` | CHAR(2) |  |  |  |  |
| 4 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 5 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 6 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 7 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 8 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 17 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 18 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 19 | `TRANSACTIONDATE` | DATE |  |  |  |  |
| 20 | `STOCKTRNTRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 21 | `STOCKTRNTRNDETAILNUMBER` | INTEGER | NOT NULL |  |  |  |
| 22 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 23 | `BASEPRIMARYQUANTITYINT` | INTEGER | NOT NULL |  |  |  |
| 24 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 25 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 26 | `BASESECONDARYQUANTITYINT` | INTEGER | NOT NULL |  |  |  |
| 27 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 28 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 29 | `USERPACKAGINGQUANTITYINT` | INTEGER | NOT NULL |  |  |  |
| 30 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 31 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 32 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ITEMSHEETWORKUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CODE,
       t.COST,
       t.COSTTYPE,
       t.TYPE,
       t.COMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06
FROM   DB2ADMIN.ITEMSHEETWORK t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
