# DB2ADMIN.LEAVECALENDAR

- **Module**: `HR` (high confidence — table name starts with 'LEAVE')
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `COMPANYCODE`, `CALENDARCODE`
- **FK degree**: referenced by 7 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 153989

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CALENDARCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `FROMDATE` | DATE | NOT NULL |  |  | Inclusive start of a validity period. |
| 6 | `TODATE` | DATE | NOT NULL |  |  | End of a validity period. |
| 7 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 8 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 9 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 10 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 11 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 12 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `LEAVECALENDAR.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 7

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `LEAVECALENDAR_LINE` | [`LEAVECALENDARDETAIL`](../HR/LEAVECALENDARDETAIL.md) | `LEAVECALENDARCOMPANYCODE`, `LEAVECALENDARCALENDARCODE` | `LEAVECALENDARDETAIL.LEAVECALENDARCOMPANYCODE = LEAVECALENDAR.COMPANYCODE AND LEAVECALENDARDETAIL.LEAVECALENDARCALENDARCODE = LEAVECALENDAR.CALENDARCODE` |
| `LEAVECALENDAR_LEAVECALENDARCODE` | [`FULLANDFINAL`](../HR/FULLANDFINAL.md) | `COMPANYCODE`, `LEAVECALENDARCODECALENDARCODE` | `FULLANDFINAL.COMPANYCODE = LEAVECALENDAR.COMPANYCODE AND FULLANDFINAL.LEAVECALENDARCODECALENDARCODE = LEAVECALENDAR.CALENDARCODE` |
| `LEAVECALENDAR_LEAVECALENDAR` | [`LEAVEBALANCE`](../HR/LEAVEBALANCE.md) | `COMPANYCODE`, `LEAVECALENDARCALENDARCODE` | `LEAVEBALANCE.COMPANYCODE = LEAVECALENDAR.COMPANYCODE AND LEAVEBALANCE.LEAVECALENDARCALENDARCODE = LEAVECALENDAR.CALENDARCODE` |
| `LEAVECALENDAR_LEAVECALENDAR` | [`LEAVEENCASHMENT`](../HR/LEAVEENCASHMENT.md) | `COMPANYCODE`, `LEAVECALENDARCALENDARCODE` | `LEAVEENCASHMENT.COMPANYCODE = LEAVECALENDAR.COMPANYCODE AND LEAVEENCASHMENT.LEAVECALENDARCALENDARCODE = LEAVECALENDAR.CALENDARCODE` |
| `LEAVECALENDAR_LEAVECALENDAR` | [`REIMBURSEMENTCLAIMDETAIL`](../HR/REIMBURSEMENTCLAIMDETAIL.md) | `REIMBURSEMENTCLAIMCOMPANYCODE`, `LEAVECALENDARCALENDARCODE` | `REIMBURSEMENTCLAIMDETAIL.REIMBURSEMENTCLAIMCOMPANYCODE = LEAVECALENDAR.COMPANYCODE AND REIMBURSEMENTCLAIMDETAIL.LEAVECALENDARCALENDARCODE = LEAVECALENDAR.CALENDARCODE` |
| `LEAVECALENDAR_LEAVECALENDAR` | [`LEAVECANCELLATION`](../HR/LEAVECANCELLATION.md) | `COMPANYCODE`, `LEAVECALENDARCALENDARCODE` | `LEAVECANCELLATION.COMPANYCODE = LEAVECALENDAR.COMPANYCODE AND LEAVECANCELLATION.LEAVECALENDARCALENDARCODE = LEAVECALENDAR.CALENDARCODE` |
| `LEAVECALENDAR_LEAVECALENDAR` | [`LEAVETRANSACTION`](../HR/LEAVETRANSACTION.md) | `COMPANYCODE`, `LEAVECALENDARCALENDARCODE` | `LEAVETRANSACTION.COMPANYCODE = LEAVECALENDAR.COMPANYCODE AND LEAVETRANSACTION.LEAVECALENDARCALENDARCODE = LEAVECALENDAR.CALENDARCODE` |

## Indexes

- `LEAVECALENDARUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CALENDARCODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.FROMDATE,
       t.TODATE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC
FROM   DB2ADMIN.LEAVECALENDAR t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
