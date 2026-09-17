# DB2ADMIN.WRKFINBALANCE

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 45
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `LINENO`, `ASONDATE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 178313

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 2 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `BSLINETEMCODE` | CHAR(10) |  |  |  |  |
| 4 | `BSLINETEMCODEFATHER` | CHAR(10) |  |  |  |  |
| 5 | `BSLINETEMDESC` | VARCHAR(200) |  |  |  |  |
| 6 | `BPFLAG` | INTEGER | NOT NULL |  |  |  |
| 7 | `CALFLAG` | INTEGER | NOT NULL |  |  |  |
| 8 | `SEQUENCENO` | DECIMAL(6,0) |  |  |  |  |
| 9 | `ISHEADING` | SMALLINT | NOT NULL |  |  |  |
| 10 | `CURRENTYEARAMT` | DECIMAL(18,5) |  |  |  |  |
| 11 | `PREVOIUSYEARAMT` | DECIMAL(18,5) |  |  |  |  |
| 12 | `BUSINESSUNIT` | CHAR(10) |  |  |  |  |
| 13 | `ASONDATE` | DATE | NOT NULL | PK | primary_key |  |
| 14 | `ORIGINALASONDATE` | DATE |  |  |  |  |
| 15 | `GLCODE` | CHAR(20) |  |  |  |  |
| 16 | `PREVDATE` | DATE |  |  |  |  |
| 17 | `BSTEMPLATECODE` | CHAR(10) |  |  |  |  |
| 18 | `CLZGGLBAL` | DECIMAL(18,5) |  |  |  |  |
| 19 | `GLSUM` | DECIMAL(18,5) |  |  |  |  |
| 20 | `PROCREDITAMT` | DECIMAL(18,5) |  |  |  |  |
| 21 | `PRODEBITAMT` | DECIMAL(18,5) |  |  |  |  |
| 22 | `TOTPROVAMT` | DECIMAL(18,5) |  |  |  |  |
| 23 | `FINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 24 | `PROVGLAMT` | DECIMAL(18,5) |  |  |  |  |
| 25 | `PREVFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 26 | `YEARFLAG` | SMALLINT | NOT NULL |  |  |  |
| 27 | `CONSOLIDATIONCURRENCY` | CHAR(4) |  |  |  |  |
| 28 | `COMPANYCURRENCY` | CHAR(4) |  |  |  |  |
| 29 | `GLDESC` | VARCHAR(200) |  |  |  |  |
| 30 | `CONSOLIDATIONCHECK` | SMALLINT | NOT NULL |  |  |  |
| 31 | `PREVOIUSYEARAMTCONSOL` | DECIMAL(18,5) |  |  |  |  |
| 32 | `CURRENTYEARAMTCONSOL` | DECIMAL(18,5) |  |  |  |  |
| 33 | `CLZGGLBALCONSOL` | DECIMAL(18,5) |  |  |  |  |
| 34 | `GLSUMCONSOL` | DECIMAL(18,5) |  |  |  |  |
| 35 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 36 | `OBGL` | DECIMAL(18,5) |  |  |  |  |
| 37 | `GLTRANSDR` | DECIMAL(18,5) |  |  |  |  |
| 38 | `GLTRANSCR` | DECIMAL(18,5) |  |  |  |  |
| 39 | `OBGLSUM` | DECIMAL(18,5) |  |  |  |  |
| 40 | `TRANSDRGLSUM` | DECIMAL(18,5) |  |  |  |  |
| 41 | `TRANSCRGLSUM` | DECIMAL(18,5) |  |  |  |  |
| 42 | `REPORTBY` | CHAR(2) |  |  |  |  |
| 43 | `MONTH` | CHAR(12) |  |  |  |  |
| 44 | `WRKPERIOD` | CHAR(100) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKFINBALANCEUID` (ABSUNIQUEID)
- `INDEX1` (CREATIONTIMESTAMP, BSLINETEMCODEFATHER, GLCODE, CLZGGLBAL)
- `INDEX2` (CREATIONTIMESTAMP, COMPANYCODE, BSLINETEMCODEFATHER, GLCODE, CLZGGLBALCONSOL)
- `INDEX3` (CREATIONTIMESTAMP, BSLINETEMCODE, GLCODE, GLSUM)
- `INDEX4` (GLSUMCONSOL, CREATIONTIMESTAMP, COMPANYCODE, BSLINETEMCODE, GLCODE)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CREATIONTIMESTAMP,
       t.LINENO,
       t.BSLINETEMCODE,
       t.BSLINETEMCODEFATHER,
       t.BSLINETEMDESC,
       t.BPFLAG,
       t.CALFLAG,
       t.SEQUENCENO,
       t.ISHEADING,
       t.CURRENTYEARAMT,
       t.PREVOIUSYEARAMT
FROM   DB2ADMIN.WRKFINBALANCE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
