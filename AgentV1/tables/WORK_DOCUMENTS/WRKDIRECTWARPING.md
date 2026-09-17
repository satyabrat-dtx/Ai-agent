# DB2ADMIN.WRKDIRECTWARPING

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 130822

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 2 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `CONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 4 | `CONTAINERCODE` | CHAR(20) |  |  |  |  |
| 5 | `CONTAINERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 6 | `CONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 7 | `BEAMNO` | CHAR(15) |  |  |  |  |
| 8 | `ENDSPERSECTION` | INTEGER | NOT NULL |  |  |  |
| 9 | `BEAMLENGTH` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 10 | `STARTTIME` | TIME |  |  |  |  |
| 11 | `ENDTIME` | TIME |  |  |  |  |
| 12 | `GROSSWEIGHT` | DECIMAL(6,2) |  |  |  |  |
| 13 | `MACHINESPEED` | CHAR(4) |  |  |  |  |
| 14 | `BEAMSTATUS` | CHAR(50) |  |  |  |  |
| 15 | `YARNBREAKAGEENTRYEVENTCODE` | CHAR(3) |  |  |  |  |
| 16 | `REMARKS` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CREATIONTIMESTAMP,
       t.LINENO,
       t.CONTAINERITEMTYPECODE,
       t.CONTAINERCODE,
       t.CONTAINERCOMPANYCODE,
       t.CONTAINERSUBCODE01,
       t.BEAMNO,
       t.ENDSPERSECTION,
       t.BEAMLENGTH,
       t.STARTTIME,
       t.ENDTIME
FROM   DB2ADMIN.WRKDIRECTWARPING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
