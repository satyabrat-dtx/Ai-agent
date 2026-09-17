# DB2ADMIN.WRKCOSTSIMPROFITELEMENTS

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `COMPANYCODE`, `UNIQUEID`, `INQUIRYSEQUENCE`, `PROFITSETCODE`, `PROFITELEMENTCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 196607

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `UNIQUEID` | BIGINT | NOT NULL | PK | primary_key |  |
| 2 | `INQUIRYSEQUENCE` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 3 | `PROFITSETCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `PROFITELEMENTCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 5 | `PROFITELEMENTDESC` | VARCHAR(200) |  |  |  |  |
| 6 | `PROFITSEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 7 | `DISPLAYSEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 8 | `FINALPRICECONTRIBUTION` | CHAR(1) |  |  |  |  |
| 9 | `VALUE` | DECIMAL(18,5) |  |  |  |  |
| 10 | `SUBUNIQUEID` | INTEGER | NOT NULL |  |  |  |
| 11 | `INPUTFROM` | CHAR(1) |  |  |  |  |
| 12 | `PROFIT` | SMALLINT | NOT NULL |  |  |  |
| 13 | `COSTLEVELCODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.UNIQUEID,
       t.INQUIRYSEQUENCE,
       t.PROFITSETCODE,
       t.PROFITELEMENTCODE,
       t.PROFITELEMENTDESC,
       t.PROFITSEQUENCE,
       t.DISPLAYSEQUENCE,
       t.FINALPRICECONTRIBUTION,
       t.VALUE,
       t.SUBUNIQUEID,
       t.INPUTFROM
FROM   DB2ADMIN.WRKCOSTSIMPROFITELEMENTS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
