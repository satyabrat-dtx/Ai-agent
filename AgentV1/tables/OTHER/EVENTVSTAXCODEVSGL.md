# DB2ADMIN.EVENTVSTAXCODEVSGL

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 24
- **Primary key**: `COMPANYCODE`, `EVENTCODE`, `TAXCODE`, `INPUTCAPITAL`, `NEXTYEARPOSTED`, `EFFECTIVEFROMDATE`
- **FK degree**: referenced by 0 constraint(s), references 6 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 124038

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `EVENTCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `TAXCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `GLCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 4 | `GLCODE` | CHAR(20) |  | FK | foreign_key |  |
| 5 | `DEBITGLCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 6 | `DEBITGLCODE` | CHAR(20) |  | FK | foreign_key |  |
| 7 | `GLDIFFERENCECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `GLDIFFERENCECODE` | CHAR(20) |  | FK | foreign_key |  |
| 9 | `CREDITGLCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 10 | `CREDITGLCODE` | CHAR(20) |  | FK | foreign_key |  |
| 11 | `INPUTCAPITAL` | INTEGER | NOT NULL | PK | primary_key |  |
| 12 | `NEXTYEARPOSTED` | INTEGER | NOT NULL | PK | primary_key |  |
| 13 | `EFFECTIVEFROMDATE` | DATE | NOT NULL | PK | primary_key |  |
| 14 | `EFFECTIVETODATE` | DATE |  |  |  |  |
| 15 | `POSTINGFLAG` | INTEGER | NOT NULL |  |  |  |
| 16 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 17 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 18 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 19 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 20 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 21 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 22 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 23 | `MANUALCLOSURE` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 6

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `EVENTVSTAXCODEVSGL.COMPANYCODE = COMPANY.CODE` |
| `EVENTMASTER_EVENT` | `EVENTCODE` | [`EVENTMASTER`](../CORE_MASTER/EVENTMASTER.md) | `CODE` | RESTRICT | `EVENTVSTAXCODEVSGL.EVENTCODE = EVENTMASTER.CODE` |
| `GLMASTER_CREDITGL` | `CREDITGLCOMPANYCODE`, `CREDITGLCODE` | [`GLMASTER`](../CORE_MASTER/GLMASTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `EVENTVSTAXCODEVSGL.CREDITGLCOMPANYCODE = GLMASTER.COMPANYCODE AND EVENTVSTAXCODEVSGL.CREDITGLCODE = GLMASTER.CODE` |
| `GLMASTER_DEBITGL` | `DEBITGLCOMPANYCODE`, `DEBITGLCODE` | [`GLMASTER`](../CORE_MASTER/GLMASTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `EVENTVSTAXCODEVSGL.DEBITGLCOMPANYCODE = GLMASTER.COMPANYCODE AND EVENTVSTAXCODEVSGL.DEBITGLCODE = GLMASTER.CODE` |
| `GLMASTER_GL` | `GLCOMPANYCODE`, `GLCODE` | [`GLMASTER`](../CORE_MASTER/GLMASTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `EVENTVSTAXCODEVSGL.GLCOMPANYCODE = GLMASTER.COMPANYCODE AND EVENTVSTAXCODEVSGL.GLCODE = GLMASTER.CODE` |
| `GLMASTER_GLDIFFERENCE` | `GLDIFFERENCECOMPANYCODE`, `GLDIFFERENCECODE` | [`GLMASTER`](../CORE_MASTER/GLMASTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `EVENTVSTAXCODEVSGL.GLDIFFERENCECOMPANYCODE = GLMASTER.COMPANYCODE AND EVENTVSTAXCODEVSGL.GLDIFFERENCECODE = GLMASTER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EVENTVSTAXCODEVSGLUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.EVENTCODE,
       t.TAXCODE,
       t.GLCOMPANYCODE,
       t.GLCODE,
       t.DEBITGLCOMPANYCODE,
       t.DEBITGLCODE,
       t.GLDIFFERENCECOMPANYCODE,
       t.GLDIFFERENCECODE,
       t.CREDITGLCOMPANYCODE,
       t.CREDITGLCODE,
       t.INPUTCAPITAL
FROM   DB2ADMIN.EVENTVSTAXCODEVSGL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
