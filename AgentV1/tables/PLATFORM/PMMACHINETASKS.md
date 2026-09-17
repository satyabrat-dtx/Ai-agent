# DB2ADMIN.PMMACHINETASKS

- **Module**: `PLATFORM` (low confidence — FK neighbourhood: 1 of 1 related tables are PLATFORM)
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `COMPANYCODE`, `PMBOMCOUNTERCODE`, `PMBOMCODE`, `PMPRVMNTCOUNTERCODE`, `PMPRVMNTCODE`, `PMPRVMNTDETAILSLINENO`, `PMPRVMNTDETAILSACTIVITYCNTCOD`, `PMPRVMNTDETAILSACTIVITYCODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 108741

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `PMBOMCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PMBOMCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `PMPRVMNTCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `PMPRVMNTCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `PMPRVMNTDETAILSLINENO` | DECIMAL(10,0) | NOT NULL | PK | primary_key |  |
| 6 | `PMPRVMNTDETAILSACTIVITYCNTCOD` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 7 | `PMPRVMNTDETAILSACTIVITYCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 8 | `LASTDATE` | DATE | NOT NULL |  |  |  |
| 9 | `NEXTDATE` | DATE | NOT NULL |  |  |  |
| 10 | `RESPONSIBLEOFSCHEDULINGUSERID` | CHAR(50) |  | FK | foreign_key |  |
| 11 | `RESPONSIBLEUSERID` | CHAR(50) |  | FK | foreign_key |  |
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
| `ABSUSERDEF_RESPONSIBLE` | `RESPONSIBLEUSERID` | [`ABSUSERDEF`](../PLATFORM/ABSUSERDEF.md) | `USERID` | RESTRICT | `PMMACHINETASKS.RESPONSIBLEUSERID = ABSUSERDEF.USERID` |
| `ABSUSERDEF_RESPONSIBLEOFSCHEDULING` | `RESPONSIBLEOFSCHEDULINGUSERID` | [`ABSUSERDEF`](../PLATFORM/ABSUSERDEF.md) | `USERID` | RESTRICT | `PMMACHINETASKS.RESPONSIBLEOFSCHEDULINGUSERID = ABSUSERDEF.USERID` |
| `PMBOM_PMBOM` | `COMPANYCODE`, `PMBOMCOUNTERCODE`, `PMBOMCODE` | [`PMBOM`](../CORE_MASTER/PMBOM.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `PMMACHINETASKS.COMPANYCODE = PMBOM.COMPANYCODE AND PMMACHINETASKS.PMBOMCOUNTERCODE = PMBOM.COUNTERCODE AND PMMACHINETASKS.PMBOMCODE = PMBOM.CODE` |
| `PMPRVMNT_PMPRVMNT` | `COMPANYCODE`, `PMPRVMNTCOUNTERCODE`, `PMPRVMNTCODE` | [`PMPRVMNT`](../PLATFORM/PMPRVMNT.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `PMMACHINETASKS.COMPANYCODE = PMPRVMNT.COMPANYCODE AND PMMACHINETASKS.PMPRVMNTCOUNTERCODE = PMPRVMNT.COUNTERCODE AND PMMACHINETASKS.PMPRVMNTCODE = PMPRVMNT.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PMMACHINETASKSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PMBOMCOUNTERCODE,
       t.PMBOMCODE,
       t.PMPRVMNTCOUNTERCODE,
       t.PMPRVMNTCODE,
       t.PMPRVMNTDETAILSLINENO,
       t.PMPRVMNTDETAILSACTIVITYCNTCOD,
       t.PMPRVMNTDETAILSACTIVITYCODE,
       t.LASTDATE,
       t.NEXTDATE,
       t.RESPONSIBLEOFSCHEDULINGUSERID,
       t.RESPONSIBLEUSERID
FROM   DB2ADMIN.PMMACHINETASKS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
