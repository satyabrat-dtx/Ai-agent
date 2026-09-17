# DB2ADMIN.WRKGMTCARTONSHIPPINGSUMMARY

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 46
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`, `CARTONCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 197296

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 2 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 3 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 5 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 6 | `COLORCODE` | CHAR(10) |  |  |  |  |
| 7 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 8 | `CARTONCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 9 | `NUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 10 | `SALESORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 11 | `SALESORDERCODE` | CHAR(15) |  |  |  |  |
| 12 | `SALESORDERLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 13 | `SALESORDERLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 14 | `SALORDLINECOMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 15 | `PACKINGGROUP` | CHAR(15) |  |  |  |  |
| 16 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 17 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 23 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 24 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 25 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 26 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 27 | `CARTONQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 28 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 29 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 30 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 31 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 32 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 33 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 34 | `NOOFCARTONS` | DECIMAL(11,0) |  |  |  |  |
| 35 | `PRODUCTSUBCODE01` | CHAR(20) |  |  |  |  |
| 36 | `PRODUCTSUBCODE02` | CHAR(10) |  |  |  |  |
| 37 | `PRODUCTSUBCODE03` | CHAR(10) |  |  |  |  |
| 38 | `PRODUCTSUBCODE04` | CHAR(10) |  |  |  |  |
| 39 | `PRODUCTSUBCODE05` | CHAR(10) |  |  |  |  |
| 40 | `PRODUCTSUBCODE06` | CHAR(10) |  |  |  |  |
| 41 | `PRODUCTSUBCODE07` | CHAR(10) |  |  |  |  |
| 42 | `PRODUCTSUBCODE08` | CHAR(10) |  |  |  |  |
| 43 | `PRODUCTSUBCODE09` | CHAR(10) |  |  |  |  |
| 44 | `PRODUCTSUBCODE10` | CHAR(10) |  |  |  |  |
| 45 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKGMTCRTSHIPPINGSUMMARYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.COLORCODE,
       t.QUANTITY,
       t.CARTONCODE,
       t.NUMBERID,
       t.SALESORDERCOUNTERCODE,
       t.SALESORDERCODE
FROM   DB2ADMIN.WRKGMTCARTONSHIPPINGSUMMARY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
