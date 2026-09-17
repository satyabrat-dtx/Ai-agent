# DB2ADMIN.ITEMCOMMENTS

- **Module**: `ITEM_MASTER` (high confidence — table name starts with 'ITEM')
- **Roles**: `business_data`
- **Columns**: 21
- **Primary key**: `ORIGIN`, `CODE`, `COMPANYCODE`, `ITEMTYPEAFICODE`, `SUBCODE01`, `SUBCODE02`, `SUBCODE03`, `SUBCODE04`, `SUBCODE05`, `SUBCODE06`, `SUBCODE07`, `SUBCODE08`, `SUBCODE09`, `SUBCODE10`, `SUFFIXCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 215424

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ORIGIN` | INTEGER | NOT NULL | PK | primary_key |  |
| 1 | `CODE` | CHAR(12) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 4 | `ITEMTYPEAFICODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 5 | `REPORTTYPE` | CHAR(90) |  |  |  |  |
| 6 | `SUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 7 | `SUBCODE02` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 8 | `SUBCODE03` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 9 | `SUBCODE04` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 10 | `SUBCODE05` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 11 | `SUBCODE06` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 12 | `SUBCODE07` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 13 | `SUBCODE08` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 14 | `SUBCODE09` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 15 | `SUBCODE10` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 16 | `SUFFIXCODE` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 17 | `COMMENTTEXT` | LONG VARCHAR | NOT NULL |  |  |  |
| 18 | `COMMENTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 19 | `CANCELED` | SMALLINT | NOT NULL |  |  |  |
| 20 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ITEMCOMMENTSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ORIGIN,
       t.CODE,
       t.COMPANYCODE,
       t.ITEMTYPEAFICOMPANYCODE,
       t.ITEMTYPEAFICODE,
       t.REPORTTYPE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06
FROM   DB2ADMIN.ITEMCOMMENTS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
