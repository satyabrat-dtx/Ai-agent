# DB2ADMIN.WRKPROJECTBUDGETCREATOR

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 57
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`, `SUBLINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 190965

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CHOOSE` | SMALLINT | NOT NULL |  |  |  |
| 1 | `EXPLODE` | SMALLINT | NOT NULL |  |  |  |
| 2 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 3 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 4 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `SUBLINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 7 | `COUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 8 | `COUNTERCODE` | CHAR(8) |  |  |  |  |
| 9 | `CODE` | CHAR(15) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 10 | `ORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 11 | `ORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 12 | `COMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 13 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 14 | `ORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 15 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 16 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 17 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 18 | `SUBCODE01` | CHAR(20) | NOT NULL |  | generic_classification_code |  |
| 19 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 23 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 24 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 25 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 26 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 27 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 28 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 29 | `ITEMDESCRIPTION` | CHAR(200) |  |  |  |  |
| 30 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 31 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 32 | `BOMSUBCODE01` | CHAR(20) |  |  |  |  |
| 33 | `BOMSUBCODE02` | CHAR(10) |  |  |  |  |
| 34 | `BOMSUBCODE03` | CHAR(10) |  |  |  |  |
| 35 | `BOMSUBCODE04` | CHAR(10) |  |  |  |  |
| 36 | `BOMSUBCODE05` | CHAR(10) |  |  |  |  |
| 37 | `BOMSUBCODE06` | CHAR(10) |  |  |  |  |
| 38 | `BOMSUBCODE07` | CHAR(10) |  |  |  |  |
| 39 | `BOMSUBCODE08` | CHAR(10) |  |  |  |  |
| 40 | `BOMSUBCODE09` | CHAR(10) |  |  |  |  |
| 41 | `BOMSUBCODE10` | CHAR(10) |  |  |  |  |
| 42 | `BOMSUFFIXCODE` | CHAR(20) |  |  |  |  |
| 43 | `RTGSUBCODE01` | CHAR(20) |  |  |  |  |
| 44 | `RTGSUBCODE02` | CHAR(10) |  |  |  |  |
| 45 | `RTGSUBCODE03` | CHAR(10) |  |  |  |  |
| 46 | `RTGSUBCODE04` | CHAR(10) |  |  |  |  |
| 47 | `RTGSUBCODE05` | CHAR(10) |  |  |  |  |
| 48 | `RTGSUBCODE06` | CHAR(10) |  |  |  |  |
| 49 | `RTGSUBCODE07` | CHAR(10) |  |  |  |  |
| 50 | `RTGSUBCODE08` | CHAR(10) |  |  |  |  |
| 51 | `RTGSUBCODE09` | CHAR(10) |  |  |  |  |
| 52 | `RTGSUBCODE10` | CHAR(10) |  |  |  |  |
| 53 | `RTGSUFFIXCODE` | CHAR(20) |  |  |  |  |
| 54 | `RTGNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 55 | `BOMNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 56 | `ALREADYEXPLODED` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CHOOSE,
       t.EXPLODE,
       t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.SUBLINE,
       t.COMPANYCODE,
       t.COUNTERCOMPANYCODE,
       t.COUNTERCODE,
       t.CODE,
       t.ORDERLINE,
       t.ORDERSUBLINE
FROM   DB2ADMIN.WRKPROJECTBUDGETCREATOR t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
