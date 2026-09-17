# DB2ADMIN.WRKWAREHOUSEENTRY

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 36
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `ELEMENTSUBCODEKEY`, `ELEMENTCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 128605

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `ELEMENTSUBCODEKEY` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 3 | `ELEMENTCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 4 | `DECOSUBCODE01` | CHAR(20) |  |  |  |  |
| 5 | `DECOSUBCODE02` | CHAR(10) |  |  |  |  |
| 6 | `DECOSUBCODE03` | CHAR(10) |  |  |  |  |
| 7 | `DECOSUBCODE04` | CHAR(10) |  |  |  |  |
| 8 | `DECOSUBCODE05` | CHAR(10) |  |  |  |  |
| 9 | `DECOSUBCODE06` | CHAR(10) |  |  |  |  |
| 10 | `DECOSUBCODE07` | CHAR(10) |  |  |  |  |
| 11 | `DECOSUBCODE08` | CHAR(10) |  |  |  |  |
| 12 | `DECOSUBCODE09` | CHAR(10) |  |  |  |  |
| 13 | `DECOSUBCODE10` | CHAR(10) |  |  |  |  |
| 14 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 15 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 16 | `ITEMCODE` | CHAR(120) |  |  |  |  |
| 17 | `DEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 18 | `DEMANDCODE` | CHAR(15) |  |  |  |  |
| 19 | `LOTCODE` | CHAR(10) |  |  |  |  |
| 20 | `CONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 21 | `CONTAINERITEMTYPECODE` | CHAR(10) |  |  |  |  |
| 22 | `CONTAINERSUBCODE01` | CHAR(15) |  |  |  |  |
| 23 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 24 | `REJECTEDQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 25 | `UOMCODE` | CHAR(3) |  |  |  |  |
| 26 | `ORIGINALQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 27 | `LAYNUM` | CHAR(15) |  |  |  |  |
| 28 | `SELECTED` | INTEGER | NOT NULL |  |  |  |
| 29 | `UNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 30 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 31 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 32 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 33 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 34 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 35 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKWAREHOUSEENTRYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.ELEMENTSUBCODEKEY,
       t.ELEMENTCODE,
       t.DECOSUBCODE01,
       t.DECOSUBCODE02,
       t.DECOSUBCODE03,
       t.DECOSUBCODE04,
       t.DECOSUBCODE05,
       t.DECOSUBCODE06,
       t.DECOSUBCODE07,
       t.DECOSUBCODE08
FROM   DB2ADMIN.WRKWAREHOUSEENTRY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
