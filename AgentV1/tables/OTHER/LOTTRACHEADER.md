# DB2ADMIN.LOTTRACHEADER

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `COMPANYCODE`, `ITEMTYPECODE`, `DECOSUBCODE01`, `DECOSUBCODE02`, `DECOSUBCODE03`, `DECOSUBCODE04`, `DECOSUBCODE05`, `DECOSUBCODE06`, `DECOSUBCODE07`, `DECOSUBCODE08`, `DECOSUBCODE09`, `DECOSUBCODE10`, `LOTCODE`, `QUALITYLEVELCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 112765

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONDATE` | DATE | NOT NULL |  |  |  |
| 1 | `CREATIONTIME` | TIME |  |  |  |  |
| 2 | `CREATIONUSER` | CHAR(50) | NOT NULL |  | audit | User who created the row (audit). |
| 3 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 5 | `DECOSUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 6 | `DECOSUBCODE02` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 7 | `DECOSUBCODE03` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 8 | `DECOSUBCODE04` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 9 | `DECOSUBCODE05` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 10 | `DECOSUBCODE06` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 11 | `DECOSUBCODE07` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 12 | `DECOSUBCODE08` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 13 | `DECOSUBCODE09` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 14 | `DECOSUBCODE10` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 15 | `LOTCODE` | CHAR(35) | NOT NULL | PK | primary_key |  |
| 16 | `QUALITYLEVELCODE` | DECIMAL(2,0) | NOT NULL | PK | primary_key |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONDATE,
       t.CREATIONTIME,
       t.CREATIONUSER,
       t.COMPANYCODE,
       t.ITEMTYPECODE,
       t.DECOSUBCODE01,
       t.DECOSUBCODE02,
       t.DECOSUBCODE03,
       t.DECOSUBCODE04,
       t.DECOSUBCODE05,
       t.DECOSUBCODE06,
       t.DECOSUBCODE07
FROM   DB2ADMIN.LOTTRACHEADER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
