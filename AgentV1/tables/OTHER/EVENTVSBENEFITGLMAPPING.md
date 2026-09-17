# DB2ADMIN.EVENTVSBENEFITGLMAPPING

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `COMPANYCODE`, `EVENTCODE`, `DIVISIONCODE`, `SCHEMETYPECODE`, `BENEFITGLCOMPANYCODE`, `BENEFITGLCODE`, `EFFECTIVEFROMDATE`
- **FK degree**: referenced by 0 constraint(s), references 6 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 121672

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `EVENTCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key | Division within a company; second-level organisational discriminator. |
| 3 | `SCHEMETYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `BENEFITGLCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `BENEFITGLCODE` | CHAR(20) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `DEBITGLCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 7 | `DEBITGLCODE` | CHAR(20) |  | FK | foreign_key |  |
| 8 | `EFFECTIVEFROMDATE` | DATE | NOT NULL | PK | primary_key |  |
| 9 | `EFFECTIVETODATE` | DATE |  |  |  |  |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 14 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 15 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 6

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `EVENTVSBENEFITGLMAPPING.COMPANYCODE = COMPANY.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `EVENTVSBENEFITGLMAPPING.COMPANYCODE = DIVISION.COMPANYCODE AND EVENTVSBENEFITGLMAPPING.DIVISIONCODE = DIVISION.CODE` |
| `EVENTMASTER_EVENT` | `EVENTCODE` | [`EVENTMASTER`](../CORE_MASTER/EVENTMASTER.md) | `CODE` | RESTRICT | `EVENTVSBENEFITGLMAPPING.EVENTCODE = EVENTMASTER.CODE` |
| `GLMASTER_BENEFITGL` | `BENEFITGLCOMPANYCODE`, `BENEFITGLCODE` | [`GLMASTER`](../CORE_MASTER/GLMASTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `EVENTVSBENEFITGLMAPPING.BENEFITGLCOMPANYCODE = GLMASTER.COMPANYCODE AND EVENTVSBENEFITGLMAPPING.BENEFITGLCODE = GLMASTER.CODE` |
| `GLMASTER_DEBITGL` | `DEBITGLCOMPANYCODE`, `DEBITGLCODE` | [`GLMASTER`](../CORE_MASTER/GLMASTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `EVENTVSBENEFITGLMAPPING.DEBITGLCOMPANYCODE = GLMASTER.COMPANYCODE AND EVENTVSBENEFITGLMAPPING.DEBITGLCODE = GLMASTER.CODE` |
| `SCHEMETYPE_SCHEMETYPE` | `COMPANYCODE`, `SCHEMETYPECODE` | [`SCHEMETYPE`](../OTHER/SCHEMETYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `EVENTVSBENEFITGLMAPPING.COMPANYCODE = SCHEMETYPE.COMPANYCODE AND EVENTVSBENEFITGLMAPPING.SCHEMETYPECODE = SCHEMETYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EVENTVSBENEFITGLMAPPINGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.EVENTCODE,
       t.DIVISIONCODE,
       t.SCHEMETYPECODE,
       t.BENEFITGLCOMPANYCODE,
       t.BENEFITGLCODE,
       t.DEBITGLCOMPANYCODE,
       t.DEBITGLCODE,
       t.EFFECTIVEFROMDATE,
       t.EFFECTIVETODATE,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.EVENTVSBENEFITGLMAPPING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
