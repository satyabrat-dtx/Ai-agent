# DB2ADMIN.WRKLOTTRACREVERSE

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 38
- **Primary key**: `COMPANYCODE`, `ITEMTYPECODE`, `DECOSUBCODE01`, `DECOSUBCODE02`, `DECOSUBCODE03`, `DECOSUBCODE04`, `DECOSUBCODE05`, `DECOSUBCODE06`, `DECOSUBCODE07`, `DECOSUBCODE08`, `DECOSUBCODE09`, `DECOSUBCODE10`, `LOTCODE`, `QUALITYLEVELCODE`, `DEVELITEMTYPECODE`, `DEVELDECOSUBCODE01`, `DEVELDECOSUBCODE02`, `DEVELDECOSUBCODE03`, `DEVELDECOSUBCODE04`, `DEVELDECOSUBCODE05`, `DEVELDECOSUBCODE06`, `DEVELDECOSUBCODE07`, `DEVELDECOSUBCODE08`, `DEVELDECOSUBCODE09`, `DEVELDECOSUBCODE10`, `DEVELLOTCODE`, `DEVELQUALITYLEVELCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 113215

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONDATE` | DATE | NOT NULL |  |  |  |
| 1 | `CREATIONTIME` | TIME |  |  |  |  |
| 2 | `CREATIONUSER` | CHAR(25) | NOT NULL |  | audit | User who created the row (audit). |
| 3 | `ALREADYDEVELOPED` | SMALLINT | NOT NULL |  |  |  |
| 4 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 5 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 6 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 7 | `DECOCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 8 | `DECOSUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 9 | `DECOSUBCODE02` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 10 | `DECOSUBCODE03` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 11 | `DECOSUBCODE04` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 12 | `DECOSUBCODE05` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 13 | `DECOSUBCODE06` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 14 | `DECOSUBCODE07` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 15 | `DECOSUBCODE08` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 16 | `DECOSUBCODE09` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 17 | `DECOSUBCODE10` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 18 | `LOTCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 19 | `LOTCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 20 | `QUALITYLEVELCODE` | DECIMAL(2,0) | NOT NULL | PK | primary_key |  |
| 21 | `DEVELITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 22 | `DEVELITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 23 | `DEVELDECOCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 24 | `DEVELDECOSUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 25 | `DEVELDECOSUBCODE02` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 26 | `DEVELDECOSUBCODE03` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 27 | `DEVELDECOSUBCODE04` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 28 | `DEVELDECOSUBCODE05` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 29 | `DEVELDECOSUBCODE06` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 30 | `DEVELDECOSUBCODE07` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 31 | `DEVELDECOSUBCODE08` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 32 | `DEVELDECOSUBCODE09` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 33 | `DEVELDECOSUBCODE10` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 34 | `DEVELLOTCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 35 | `DEVELLOTCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 36 | `DEVELQUALITYLEVELCODE` | DECIMAL(2,0) | NOT NULL | PK | primary_key |  |
| 37 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKLOTTRACREVERSEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONDATE,
       t.CREATIONTIME,
       t.CREATIONUSER,
       t.ALREADYDEVELOPED,
       t.COMPANYCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.DECOCOMPANYCODE,
       t.DECOSUBCODE01,
       t.DECOSUBCODE02,
       t.DECOSUBCODE03,
       t.DECOSUBCODE04
FROM   DB2ADMIN.WRKLOTTRACREVERSE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
