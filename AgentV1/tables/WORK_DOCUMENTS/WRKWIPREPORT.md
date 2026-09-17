# DB2ADMIN.WRKWIPREPORT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 44
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 51309

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `EXPIRATIONDATE` | DATE |  |  |  |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `COUNTERCODE` | CHAR(8) |  |  |  |  |
| 5 | `CODE` | CHAR(15) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 6 | `STEPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 7 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 8 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 9 | `ERRORVALUE` | SMALLINT | NOT NULL |  |  |  |
| 10 | `ERRORVALUECOLUMN1` | SMALLINT | NOT NULL |  |  |  |
| 11 | `ERRORVALUECOLUMN2` | SMALLINT | NOT NULL |  |  |  |
| 12 | `ERRORVALUECOLUMN3` | SMALLINT | NOT NULL |  |  |  |
| 13 | `ERRORVALUECOLUMN4` | SMALLINT | NOT NULL |  |  |  |
| 14 | `ERRORVALUECOLUMN5` | SMALLINT | NOT NULL |  |  |  |
| 15 | `ERRORVALUECOLUMN6` | SMALLINT | NOT NULL |  |  |  |
| 16 | `DEPARTMENTCODE` | CHAR(8) |  |  |  |  |
| 17 | `WORKCENTERCODE` | CHAR(8) |  |  |  |  |
| 18 | `PRODUCTNATURE` | CHAR(1) |  |  |  |  |
| 19 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 20 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 21 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 22 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 23 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 24 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 25 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 26 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 27 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 28 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 29 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 30 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 31 | `PRODUCTDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 32 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 33 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 34 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 35 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 36 | `VALUE` | DECIMAL(18,5) |  |  |  |  |
| 37 | `VALUECOLUMN1` | DECIMAL(18,5) |  |  |  |  |
| 38 | `VALUECOLUMN2` | DECIMAL(18,5) |  |  |  |  |
| 39 | `VALUECOLUMN3` | DECIMAL(18,5) |  |  |  |  |
| 40 | `VALUECOLUMN4` | DECIMAL(18,5) |  |  |  |  |
| 41 | `VALUECOLUMN5` | DECIMAL(18,5) |  |  |  |  |
| 42 | `VALUECOLUMN6` | DECIMAL(18,5) |  |  |  |  |
| 43 | `AFTERSTEP` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.LINE,
       t.EXPIRATIONDATE,
       t.COMPANYCODE,
       t.COUNTERCODE,
       t.CODE,
       t.STEPNUMBER,
       t.LOGICALWAREHOUSECOMPANYCODE,
       t.LOGICALWAREHOUSECODE,
       t.ERRORVALUE,
       t.ERRORVALUECOLUMN1,
       t.ERRORVALUECOLUMN2
FROM   DB2ADMIN.WRKWIPREPORT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
