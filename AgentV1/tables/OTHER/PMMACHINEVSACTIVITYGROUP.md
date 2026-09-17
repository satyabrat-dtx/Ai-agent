# DB2ADMIN.PMMACHINEVSACTIVITYGROUP

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `COMPANYCODE`, `MACHINECOUNTERCODE`, `MACHINECODE`, `ACTIVITYGROUPCOUNTERCODE`, `ACTIVITYGROUPCODE`, `HALLNOUSERGENERICGROUPTYPECODE`, `HALLNOCODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 89206

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `MACHINECOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `MACHINECODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `ACTIVITYGROUPCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `ACTIVITYGROUPCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `FREQUENCY` | INTEGER | NOT NULL |  |  |  |
| 6 | `HALLNOUSERGENGRPTYPECMYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 7 | `HALLNOUSERGENERICGROUPTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 8 | `HALLNOCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 9 | `LASTWORKORDERCOUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 10 | `LASTWORKORDERCODE` | CHAR(15) |  | FK | foreign_key |  |
| 11 | `LASTWORKORDERDATE` | DATE |  |  |  |  |
| 12 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 13 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 14 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 15 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PMMACHINEVSACTIVITYGROUP.COMPANYCODE = COMPANY.CODE` |
| `PMACTIVITYGROUP_ACTIVITYGROUP` | `COMPANYCODE`, `ACTIVITYGROUPCOUNTERCODE`, `ACTIVITYGROUPCODE` | [`PMACTIVITYGROUP`](../PLATFORM/PMACTIVITYGROUP.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `PMMACHINEVSACTIVITYGROUP.COMPANYCODE = PMACTIVITYGROUP.COMPANYCODE AND PMMACHINEVSACTIVITYGROUP.ACTIVITYGROUPCOUNTERCODE = PMACTIVITYGROUP.COUNTERCODE AND PMMACHINEVSACTIVITYGROUP.ACTIVITYGROUPCODE = PMACTIVITYGROUP.CODE` |
| `PMBOM_MACHINE` | `COMPANYCODE`, `MACHINECOUNTERCODE`, `MACHINECODE` | [`PMBOM`](../CORE_MASTER/PMBOM.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `PMMACHINEVSACTIVITYGROUP.COMPANYCODE = PMBOM.COMPANYCODE AND PMMACHINEVSACTIVITYGROUP.MACHINECOUNTERCODE = PMBOM.COUNTERCODE AND PMMACHINEVSACTIVITYGROUP.MACHINECODE = PMBOM.CODE` |
| `PMWORKORDER_LASTWORKORDER` | `COMPANYCODE`, `LASTWORKORDERCOUNTERCODE`, `LASTWORKORDERCODE` | [`PMWORKORDER`](../INTERNAL_ORDERS/PMWORKORDER.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `PMMACHINEVSACTIVITYGROUP.COMPANYCODE = PMWORKORDER.COMPANYCODE AND PMMACHINEVSACTIVITYGROUP.LASTWORKORDERCOUNTERCODE = PMWORKORDER.COUNTERCODE AND PMMACHINEVSACTIVITYGROUP.LASTWORKORDERCODE = PMWORKORDER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PMMACHINEVSACTIVITYGROUPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.MACHINECOUNTERCODE,
       t.MACHINECODE,
       t.ACTIVITYGROUPCOUNTERCODE,
       t.ACTIVITYGROUPCODE,
       t.FREQUENCY,
       t.HALLNOUSERGENGRPTYPECMYCODE,
       t.HALLNOUSERGENERICGROUPTYPECODE,
       t.HALLNOCODE,
       t.LASTWORKORDERCOUNTERCODE,
       t.LASTWORKORDERCODE,
       t.LASTWORKORDERDATE
FROM   DB2ADMIN.PMMACHINEVSACTIVITYGROUP t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
