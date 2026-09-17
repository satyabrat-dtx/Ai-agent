# DB2ADMIN.WRKMSESPECIFICATIONPRINTPRMS

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 21
- **Primary key**: `CREATIONTIMESTAMP`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 192517

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `PERIODIZEDCALENDARTYPECODE` | CHAR(10) |  |  |  |  |
| 3 | `PERIODIZEDCALENDARYEAR` | DECIMAL(4,0) |  |  |  |  |
| 4 | `INITIALPERIODCODE` | DECIMAL(3,0) |  |  |  |  |
| 5 | `FINALPERIODCODE` | DECIMAL(3,0) |  |  |  |  |
| 6 | `INITIALDATE` | DATE |  |  |  |  |
| 7 | `FINALDATE` | DATE |  |  |  |  |
| 8 | `INITIALSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 9 | `INITIALSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 10 | `SHOWFINALSUPPLIER` | SMALLINT | NOT NULL |  |  |  |
| 11 | `FINALSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 12 | `FINALSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 13 | `SPECIFICATIONGROUPS` | CHAR(90) |  |  |  |  |
| 14 | `PHASE1` | SMALLINT | NOT NULL |  |  |  |
| 15 | `PHASE2` | SMALLINT | NOT NULL |  |  |  |
| 16 | `REPORTABSUIXMLPATH` | CHAR(50) |  |  |  |  |
| 17 | `REPORTABSUIXMLNAME` | VARCHAR(54) |  |  |  |  |
| 18 | `REPORTCONTEXT` | CHAR(2) |  |  |  |  |
| 19 | `REPORTREPORTCODE` | CHAR(50) |  |  |  |  |
| 20 | `USERID` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.PERIODIZEDCALENDARTYPECODE,
       t.PERIODIZEDCALENDARYEAR,
       t.INITIALPERIODCODE,
       t.FINALPERIODCODE,
       t.INITIALDATE,
       t.FINALDATE,
       t.INITIALSUPPLIERTYPE,
       t.INITIALSUPPLIERCODE,
       t.SHOWFINALSUPPLIER,
       t.FINALSUPPLIERTYPE
FROM   DB2ADMIN.WRKMSESPECIFICATIONPRINTPRMS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
