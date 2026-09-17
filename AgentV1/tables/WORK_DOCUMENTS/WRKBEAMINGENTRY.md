# DB2ADMIN.WRKBEAMINGENTRY

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 130726

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 2 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `CONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 4 | `CONTAINERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 5 | `CONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 6 | `BEAMNO` | CHAR(15) |  |  |  |  |
| 7 | `BEAMLENGTH` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 8 | `STARTTIME` | TIME |  |  |  |  |
| 9 | `ENDTIME` | TIME |  |  |  |  |
| 10 | `GROSSWEIGHT` | DECIMAL(6,2) |  |  |  |  |
| 11 | `MACHINESPEED` | CHAR(4) |  |  |  |  |
| 12 | `BEAMSTATUS` | CHAR(50) |  |  |  |  |
| 13 | `REMARKS` | CHAR(50) |  |  |  |  |

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
       t.CONTAINERCOMPANYCODE,
       t.CONTAINERSUBCODE01,
       t.BEAMNO,
       t.BEAMLENGTH,
       t.STARTTIME,
       t.ENDTIME,
       t.GROSSWEIGHT,
       t.MACHINESPEED
FROM   DB2ADMIN.WRKBEAMINGENTRY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
